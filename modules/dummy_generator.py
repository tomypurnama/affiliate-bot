import random

def generate_content(keyword):
    hooks = [
        f"Gak nyangka {keyword} ini lagi viral!",
        f"Serius ini {keyword} murah banget!",
        f"Jangan beli {keyword} sebelum lihat ini!"
    ]

    desc = [
        f"{keyword} ini lagi banyak dicari karena kualitasnya bagus dan harga terjangkau.",
        f"Cocok banget buat kamu yang butuh {keyword} murah tapi berkualitas.",
        f"Produk ini lagi trending dan banyak review positif."
    ]

    return f"""
{random.choice(hooks)}

{random.choice(desc)}

🔥 {keyword.upper()} TERBAIK 2026!
"""
