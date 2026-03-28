import requests
import time
import random

# ================= CONFIG =================
TELEGRAM_TOKEN = "8641066083:AAH1NDpN7FHFg-PgQiiymREPRDGde3f8xe8"
# ==========================================

# ====== DATA KONTEN ======

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
    "Dipakai banyak orang & terbukti bagus",
]

cta = [
    "Buruan cek sebelum kehabisan!",
    "Klik sekarang juga!",
    "Jangan sampai ketinggalan!",
    "Langsung beli sekarang!",
    "Cek harga terbaru di bawah!",
]

hashtags = [
    "#produkviral", "#murahbanget", "#diskon",
    "#racunshopee", "#barangviral", "#rekomendasi"
]

# ====== GENERATOR ======

def generate_content(keyword):
    hook = random.choice(hooks).format(keyword=keyword)
    benefit_list = random.sample(benefits, 3)
    call = random.choice(cta)
    tags = " ".join(random.sample(hashtags, 3))

    return f"""
💥 {hook}

🔥 {keyword.upper()} TERLARIS!

✅ {benefit_list[0]}
✅ {benefit_list[1]}
✅ {benefit_list[2]}

👉 {call}

{tags}
"""

# ====== AFFILIATE LINK ======

def get_link(keyword):
    return f"https://shopee.co.id/search?keyword={keyword.replace(' ', '%20')}"

# ====== FORMAT ======

def format_output(keyword, content):
    return f"{content}\n\n🛒 Beli di sini:\n{get_link(keyword)}"

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

def menu():
    return {
        "keyboard": [
            ["🛍 1 Konten", "🔥 5 Konten"],
            ["📊 Contoh", "ℹ️ Bantuan"]
        ],
        "resize_keyboard": True
    }

# ====== SAMPLE ======

def sample():
    return """
🔥 SEPATU TERBAIK!

💥 Jangan beli sebelum lihat ini!

✅ Ringan
✅ Nyaman
✅ Murah

👉 Buruan cek!

🛒 https://shopee.co.id/xxx
"""

# ====== MAIN ======

def main():
    offset = None
    user_state = {}

    while True:
        updates = get_updates(offset)

        for update in updates["result"]:
            offset = update["update_id"] + 1

            try:
                msg = update["message"]
                chat_id = msg["chat"]["id"]
                text = msg.get("text", "")

                # START
                if text == "/start":
                    send_message(chat_id, "🚀 Affiliate Bot Ready!", menu())

                # MENU
                elif text == "🛍 1 Konten":
                    user_state[chat_id] = "ONE"
                    send_message(chat_id, "Masukkan nama produk:")

                elif text == "🔥 5 Konten":
                    user_state[chat_id] = "MULTI"
                    send_message(chat_id, "Masukkan nama produk:")

                elif text == "📊 Contoh":
                    send_message(chat_id, sample())

                elif text == "ℹ️ Bantuan":
                    send_message(chat_id, "Pilih menu lalu masukkan produk.")

                # INPUT
                elif chat_id in user_state:
                    keyword = text
                    mode = user_state[chat_id]

                    send_message(chat_id, "⏳ Membuat konten...")

                    if mode == "ONE":
                        content = generate_content(keyword)
                        send_message(chat_id, format_output(keyword, content))

                    elif mode == "MULTI":
                        for i in range(5):
                            content = generate_content(keyword)
                            send_message(chat_id, f"Konten {i+1}:\n{format_output(keyword, content)}")
                            time.sleep(1)

                    user_state.pop(chat_id)

            except Exception as e:
                print("Error:", e)

        time.sleep(1)

# ====== RUN ======

if __name__ == "__main__":
    main()
