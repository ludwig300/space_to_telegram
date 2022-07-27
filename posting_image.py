import telegram
import os
import argparse
import random
from dotenv import load_dotenv


def public_image(chat_id, path):
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token)
    with open(path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def createParser (random_file):
    parser = argparse.ArgumentParser(description='Program for posting image in telegram chanal')
    parser.add_argument ('chat_id', help='Look like "@testchanal0"')
    parser.add_argument ('-f', '--file', default=f'./image/{random_file}', help='Specify the path to the file. Default publication random file from "./image"')
    return parser


def main():
    load_dotenv()
    files_in_dir = os.listdir('./image')
    random_file = random.choice(files_in_dir)
    parser = createParser(random_file)
    namespace = parser.parse_args()
    public_image(namespace.chat_id, namespace.file)


if __name__ == '__main__':
    main()
