import random

hooks = [
    "Gak nyangka {keyword} ini lagi viral!",
    "Serius ini {keyword} murah banget!",
    "Jangan beli {keyword} sebelum lihat ini!",
    "{keyword} ini lagi dicari banyak orang!",
    "Ini dia {keyword} yang lagi trending!"
]

benefits = [
    "Ringan dan nyaman dipakai",
    "Harga terjangkau tapi kualitas oke",
    "Banyak review positif",
    "Cocok untuk penggunaan sehari-hari",
    "Desain modern dan keren"
]

cta = [
    "Buruan cek sebelum kehabisan!",
    "Klik sekarang juga!",
    "Jangan sampai ketinggalan!",
    "Langsung beli sekarang!",
    "Cek harga terbaru di bawah!"
]

def generate_content(keyword):
    hook = random.choice(hooks).format(keyword=keyword)
    benefit_list = random.sample(benefits, 2)
    call = random.choice(cta)

    return f"""
🔥 {keyword.upper()} TERLARIS!

{hook}

✅ {benefit_list[0]}
✅ {benefit_list[1]}

👉 {call}
"""
