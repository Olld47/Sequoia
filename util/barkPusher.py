# -*- encoding: UTF-8 -*-

import requests
import logging

url = "https://api.day.app/push"
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

def send_message(content, title, **kwargs):
    data = {
        "body": content,
        "title": title,
        "device_key": kwargs.get('key'),
        "group": kwargs.get('group'),
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        logging.info("Request successful")
    else:
        logging.error(f"Request:{data} failed with status code {response}")
