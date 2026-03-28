from utils.telegram import send_message
from handlers.affiliate_cmd import handle_affiliate
import requests
import time
from config import TELEGRAM_TOKEN

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    return requests.get(url, params=params).json()

def main():
    offset = None

    while True:
        updates = get_updates(offset)

        for update in updates["result"]:
            offset = update["update_id"] + 1

            try:
                message = update["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")

                if text.startswith("/affiliate"):
                    keyword = text.replace("/affiliate", "").strip()

                    if not keyword:
                        send_message(chat_id, "Masukkan keyword produk ya!")
                        continue

                    send_message(chat_id, "⏳ Sedang membuat konten...")

                    result = handle_affiliate(keyword)

                    send_message(chat_id, result)

            except Exception as e:
                print("Error:", e)

        time.sleep(1)

if __name__ == "__main__":
    main()
