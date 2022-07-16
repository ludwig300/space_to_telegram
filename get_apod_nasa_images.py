import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import argparse
from extension import get_extension
from download_image import download_image


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


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-c', '--count', default=1, type=int, help='Count images from NASA to download')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    nasa_api_key = os.environ['NASA_API']
    Path("image").mkdir(parents=True, exist_ok=True)
    get_nasa_images(nasa_api_key, namespace.count)


if __name__ == '__main__':
    main()