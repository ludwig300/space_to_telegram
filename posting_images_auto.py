import random
import time
import argparse
import os
from posting_image import public_image
from dotenv import load_dotenv


def publishes_files(chat_id, secs):
    while True:
        files_in_dir = os.listdir('./image')
        random.shuffle(files_in_dir)
        for file_in_dir in files_in_dir:
            path = f'image/{file_in_dir}'
            public_image(chat_id, path)
            time.sleep(secs)


def createParser ():
    parser = argparse.ArgumentParser(description='Publishes files in telegram, at a given time. Standard time 4 hours')
    parser.add_argument ('chat_id', help='Look like "@testchanal0"')
    parser.add_argument ('-t', '--timer', default=14400, type=int, help='Count secs for publication')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    publishes_files(namespace.chat_id, namespace.timer)


if __name__ == '__main__':
    main()
