from config import USE_AI
from modules.affiliate import get_affiliate_link
from modules.formatter import format_message

# pilih generator berdasarkan mode
if USE_AI:
    from modules.ai_generator import generate_content
else:
    from modules.dummy_generator import generate_content


def handle_affiliate(keyword):
    content = generate_content(keyword)
    link = get_affiliate_link(keyword)

    return format_message(content, link)
