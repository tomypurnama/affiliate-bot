from utils.telegram import send_message
from handlers.affiliate_cmd import handle_affiliate
import requests
import time
from config import TELEGRAM_TOKEN

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKENimport requests
import time
import random

# ================= CONFIG =================
TELEGRAM_TOKEN = "8641066083:AAHXgDz3x1Qnjdn-alXDjsTaa45JkWBNNlg"
USE_AI = False  # nanti ubah True kalau sudah pakai OpenAI

# ==========================================

# ====== DUMMY GENERATOR (HIGH CONVERT) ======

hooks = [
    "Gak nyangka {keyword} ini lagi viral!",
    "Serius ini {keyword} murah banget!",
    "Jangan beli {keyword} sebelum lihat ini!",
    "{keyword} ini lagi diburu banyak orang!",
    "Ini dia {keyword} yang lagi trending!",
    "Produk {keyword} ini lagi rame banget!",
    "Rahasia {keyword} yang jarang orang tahu!",
]

benefits = [
    "Ringan dan nyaman dipakai",
    "Harga terjangkau tapi kualitas oke",
    "Banyak review positif",
    "Cocok untuk penggunaan sehari-hari",
    "Desain modern dan keren",
    "Awet dan tahan lama",
    "Best seller di kategori ini",
]

cta = [
    "Buruan cek sebelum kehabisan!",
    "Klik sekarang juga!",
    "Jangan sampai ketinggalan!",
    "Langsung beli sekarang!",
    "Cek harga terbaru di bawah!",
]

hashtags = [
    "#produkviral", "#murahbanget", "#diskon", "#shopeehaul",
    "#racunshopee", "#barangviral", "#rekomendasi"
]

def generate_content(keyword):
    hook = random.choice(hooks).format(keyword=keyword)
    benefit_list = random.sample(benefits, 3)
    call = random.choice(cta)
    tags = " ".join(random.sample(hashtags, 3))

    return f"""
💥 {hook}

🔥 {keyword.upper()} TERLARIS 2026!

✅ {benefit_list[0]}
✅ {benefit_list[1]}
✅ {benefit_list[2]}

👉 {call}

{tags}
"""

# ====== AFFILIATE LINK (SIMPLE) ======

def get_affiliate_link(keyword):
    return f"https://shopee.co.id/search?keyword={keyword.replace(' ', '%20')}"

# ====== FORMAT FINAL ======

def format_message(keyword, content, link):
    return f"""
{content}

🛒 Beli di sini:
{link}
"""

# ====== TELEGRAM ======

def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }

    if keyboard:
        data["reply_markup"] = keyboard

    requests.post(url, json=data)

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    return requests.get(url, params=params).json()

# ====== UI MENU ======

def main_menu():
    return {
        "keyboard": [
            ["🛍 Generate Konten"],
            ["🔥 Contoh Output", "ℹ️ Bantuan"]
        ],
        "resize_keyboard": True
    }

# ====== SAMPLE OUTPUT (LATIHAN) ======

def sample_output():
    samples = [
        "🔥 SEPATU TERNYAMAN!\nCocok buat olahraga & santai!",
        "🔥 HEADSET GAMING MURAH!\nBass mantap & nyaman!",
        "🔥 JAM TANGAN KEREN!\nStylish & harga terjangkau!",
    ]
    return "\n\n".join(samples)

# ====== MAIN LOOP ======

def main():
    offset = None
    user_state = {}

    while True:
        updates = get_updates(offset)

        for update in updates["result"]:
            offset = update["update_id"] + 1

            try:
                message = update["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")

                # START
                if text == "/start":
                    send_message(
                        chat_id,
                        "🚀 Affiliate Bot Siap!\n\nKlik menu untuk mulai 👇",
                        main_menu()
                    )

                # MENU
                elif text == "🛍 Generate Konten":
                    user_state[chat_id] = "WAITING_KEYWORD"
                    send_message(chat_id, "Masukkan nama produk:")

                elif text == "🔥 Contoh Output":
                    send_message(chat_id, sample_output())

                elif text == "ℹ️ Bantuan":
                    send_message(chat_id, "Ketik /start lalu pilih menu.")

                # INPUT KEYWORD
                elif user_state.get(chat_id) == "WAITING_KEYWORD":
                    keyword = text

                    send_message(chat_id, "⏳ Membuat konten...")

                    content = generate_content(keyword)
                    link = get_affiliate_link(keyword)
                    result = format_message(keyword, content, link)

                    send_message(chat_id, result)

                    user_state[chat_id] = None

            except Exception as e:
                print("Error:", e)

        time.sleep(1)

# ====== RUN ======

if __name__ == "__main__":
    main()}/getUpdates"
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
