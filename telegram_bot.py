import telegram
import os
from dotenv import load_dotenv


def public_text(chat_id, text):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=text)


def public_image(chat_id, path):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token)
    bot.send_document(chat_id=chat_id, document=open(path, 'rb'))


def main():
    load_dotenv()
    # public_text('@testchanal0', 'Hello World')
    public_image('@testchanal0', 'image/nasa_apod_0.jpg')


if __name__ == '__main__':
    main()
