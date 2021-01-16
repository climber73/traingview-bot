import logging
import requests

import secrets

url = "https://api.telegram.org/bot%s/sendMessage" % secrets.TELEGRAM_BOT_API_KEY


def post_message(message):
    logging.debug("telegram: sending message [%s]" % message)
    resp = requests.get(url, params={"chat_id": secrets.TELEGRAM_CHAT_ID, "text": message}, timeout=5)
    logging.debug("telegram responded: [%s]" % resp.__dict__)
