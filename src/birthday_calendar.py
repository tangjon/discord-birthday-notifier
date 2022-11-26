import csv
from collections import defaultdict
from datetime import date, datetime

YEAR_UNDEFINED = "0000"


def _contact_parser(contacts_csv):
    with open(contacts_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            birthday = row["Birthday"]
            if birthday:
                row["Birthday"] = _format_birthday(birthday)
            yield row


def _format_birthday(day):
    if day.startswith(" --"):
        day = day.lstrip(" --")
        day = "0000-" + day
    return day


def sort_contacts(list_of_contacts):
    return sorted(list_of_contacts, key=lambda contact: datetime.strptime(contact["Birthday"][5:], "%m-%d"))


class BirthdayCalendar:
    def __init__(self, csv_path):
        self._calendar = defaultdict(list)  # day -> contacts

        contacts = _contact_parser(csv_path)
        for contact in contacts:
            birthday = contact["Birthday"]
            if birthday:
                _, mm, dd = birthday.split("-")
                self._calendar[f"{mm}{dd}"].append(contact)

    def today(self):
        today = date.today()
        key = "{:0>2d}{:0>2d}".format(today.month, today.day)
        return sort_contacts(self._calendar[key])

    def month(self):
        contacts = []
        month = date.today().month
        for key, value in self._calendar.items():
            if key.startswith("{:0>2d}".format(month)):
                contacts.extend(value)
        return sort_contacts(contacts)

    def next_month(self):
        contacts = []
        month = date.today().month
        month = month + 1 if month < 12 else 1
        for key, value in self._calendar.items():
            if key.startswith("{:0>2d}".format(month)):
                contacts.extend(value)
        return sort_contacts(contacts)
