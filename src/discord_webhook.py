import os

import requests
import configparser

dir_path = os.path.dirname(os.path.realpath(__file__))


class DiscordWebhook:
    def __init__(self, webhook_url, username, avatar_url) -> None:
        self._webhook_url = webhook_url
        self._username = username
        self._avatar_url = avatar_url

    def push(self, message):
        data = {
            "username": self._username,
            "avatar_url": self._avatar_url or "",
            "content": message
        }

        requests.post(self._webhook_url, data)


if __name__ == "__main__":
    config_parser = configparser.ConfigParser()
    config_parser.read(os.path.join(dir_path, "../config.ini"))
    config = config_parser["discord"]
    webhook = DiscordWebhook(config["birthday-web-hook"])
    webhook.push(**{
        "username": "Birthday Notifier",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/931/931950.png",
        "content": "Text message. Up to 2000 characters.",
    })
