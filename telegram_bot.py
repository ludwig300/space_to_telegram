import telegram
import os
from dotenv import load_dotenv


def public_text(chat_id, text):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=text)


def main():
    load_dotenv()
    public_text('@testchanal0', 'Hello World')


if __name__ == '__main__':
    main()
