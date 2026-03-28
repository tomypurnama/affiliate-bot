from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_content(keyword):
    prompt = f"""
    Buatkan konten affiliate untuk produk: {keyword}

    Format:
    1. Judul menarik (maks 10 kata)
    2. Deskripsi singkat (maks 3 kalimat)
    3. Hook (kalimat pembuka yang bikin penasaran)
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
