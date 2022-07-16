import requests
import argparse
from dotenv import load_dotenv
from pathlib import Path
from download_image import download_image
from extension import get_extension


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
