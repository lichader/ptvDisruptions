#!venv/bin/python3
import json
import os
import requests

chat_id = os.environ.get('TELEGRAM_CHAT_ID', '')
token = os.environ.get('TELEGRAM_TOKEN', '')
disruption_url = os.environ.get('DISRUPTION_URL', '')

message_template = "Title: {}\n\nDescription: {}\n\nfrom: {}\nto: {}"

def sendTelegramMessage(text):
    requestBody = {
        "chat_id": chat_id,
        "text": text
    }
    print("Send message: ", text)
    url = "https://api.telegram.org/bot{}/sendMessage".format(token)
    r = requests.post(url, json=requestBody)
    print(f"Response status code {r.status_code}")

def checkDisruptions(event, context):
    response = requests.get(disruption_url)
    print(f"Status code of checking disruption request is {response.status_code}")
    disruptions = json.loads(response.text)["disruptions"]["metro_train"]
    for d in disruptions:
        message_body = message_template.format(d["title"], d["description"], d["from_date"], d["to_date"])
        sendTelegramMessage(message_body)

if __name__ == "__main__":
    checkDisruptions(None, None)
