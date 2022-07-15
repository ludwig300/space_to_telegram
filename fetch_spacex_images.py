import requests
import argparse
import urllib.parse
import os
from dotenv import load_dotenv
from pathlib import Path


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(urlstring):
    parsed_url = urllib.parse.urlsplit(urlstring, scheme='', allow_fragments=True)
    unquoted_filename = urllib.parse.unquote(parsed_url[2], encoding='utf-8', errors='replace')
    splited_filename = os.path.split(unquoted_filename)
    extension = os.path.splitext(splited_filename[1])
    return extension[1]


def fetch_spacex_last_launch(id):
    url_api_spacex = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url_api_spacex)
    links_pics = response.json()['links']['flickr']['original']
    for links_number, url in enumerate(links_pics):
        path = f'image/spacex{links_number}{get_extension(url)}'
        download_image(url, path) 


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i', '--id', default='latest', help='"id" from https://api.spacexdata.com/v5/launches')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    Path("image").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(namespace.id)


if __name__ == '__main__':
    main()
