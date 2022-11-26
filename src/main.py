import configparser

from birthday_calendar import BirthdayCalendar, YEAR_UNDEFINED
from datetime import date

from discord_webhook import DiscordWebhook
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_webhook():
    config_parser = configparser.ConfigParser()
    config_parser.read(os.path.join(dir_path, "../config.ini"))
    config = config_parser["discord"]
    return DiscordWebhook(
        config["birthday-web-hook"],
        "Birthday Notifier",
        "https://cdn-icons-png.flaticon.com/512/931/931950.png",
    )


def format_contact(contact, include_age=False, include_date=False):
    today = date.today()
    name = contact["Name"]
    birthday = contact["Birthday"].split("-")
    age = today.year - int(birthday[0]) if birthday[0] != YEAR_UNDEFINED else None

    metadata = []
    if include_age:
        metadata.append(f" ({age})" if age else "")
    if include_date:
        if birthday[0] == YEAR_UNDEFINED:
            metadata.append("-".join(birthday[1:]))
        else:
            metadata.append(contact["Birthday"])
    return name + ", ".join(metadata)


def main():
    today = date.today()
    calender = BirthdayCalendar(os.path.join(dir_path, "../contacts.csv"))

    webhook = get_webhook()
    if today.day == 1:
        contacts = calender.month()
        if contacts:
            message = f"Happy {today.strftime('%B')}. Heads up the following birthdays are coming up!\n"
            birthdays = [
                "- " + format_contact(contact, include_age=True, include_date=True)
                for contact in contacts
            ]
            webhook.push(message + "\n".join(birthdays))

    contacts = calender.today()
    if contacts:
        message = "Birthdays today! Don't for get to wish Happy Birthday to\n"
        birthdays = [
            "- " + format_contact(contact, include_age=True) for contact in contacts
        ]
        webhook.push(message + "\n".join(birthdays))
    else:
        print("No birthdays today =(")


if __name__ == "__main__":
    main()
