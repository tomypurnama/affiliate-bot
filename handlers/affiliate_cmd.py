from modules.ai_generator import generate_content
from modules.affiliate import get_affiliate_link
from modules.formatter import format_message

def handle_affiliate(keyword):
    content = generate_content(keyword)
    link = get_affiliate_link(keyword)

    return format_message(content, link)
