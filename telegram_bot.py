import telegram
import os


def public_text(chat_id, text):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=text)


def public_image(chat_id, path):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token)
    bot.send_document(chat_id=chat_id, document=open(path, 'rb'))



