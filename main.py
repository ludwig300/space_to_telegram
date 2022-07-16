import requests
from pathlib import Path
import os
import datetime
from dotenv import load_dotenv
import argparse
from download_image import download_image
from extension import get_extension

def fetch_spacex_last_launch(id):
    url_api_spacex = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url_api_spacex)
    links_pics = response.json()['links']['flickr']['original']
    for links_number, url in enumerate(links_pics):
        path = f'image/spacex{links_number}{get_extension(url)}'
        download_image(url, path)
        

def get_nasa_images(nasa_key, count_images):
    payload = {
        'api_key': f'{nasa_key}',
        'count': count_images
    }
    url_api_nasa = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url_api_nasa, params=payload)
    for apod_number, apod in enumerate(response.json()):
        if apod['media_type'] in 'image':
            urlstring = apod['url']
            path = f'image/nasa_apod_{apod_number}{get_extension(urlstring)}'
            download_image(urlstring, path)
        else:
            continue


def get_epic_image(nasa_api_key):
    payload = {
        'api_key': f'{nasa_api_key}',   
    }
    url_api_epic = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url_api_epic, params=payload)
    response.raise_for_status()
    for number_epic in range(5):
        date = datetime.datetime.fromisoformat(response.json()[number_epic]['date'])
        formatted_date = date.strftime("%Y/%m/%d")
        image_name = response.json()[number_epic]['image']
        url_template = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_name}.png'
        response_new = requests.get(url_template, params=payload)
        path = f'image/{image_name}.png'
        download_image(response_new.url, path)


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i', '--id', default='latest', help='"id" from https://api.spacexdata.com/v5/launches')
    parser.add_argument ('-c', '--count', default=1, type=int, help='Count images from NASA to download')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    nasa_api_key = os.environ['NASA_API']
    Path("image").mkdir(parents=True, exist_ok=True)
    get_nasa_images(nasa_api_key, namespace.count)
    get_epic_image(nasa_api_key)
    fetch_spacex_last_launch(namespace.id)


if __name__ == '__main__':
    main()
