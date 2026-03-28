import requests
from config import TELEGRAM_TOKEN

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=data)
