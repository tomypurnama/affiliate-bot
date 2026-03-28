import json

def get_affiliate_link(keyword):
    with open("data/products.json", "r") as f:
        products = json.load(f)

    for p in products:
        if keyword.lower() in p["name"]:
            return p["link"]

    return "Link belum tersedia"
