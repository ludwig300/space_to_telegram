import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import argparse
from extension import get_extension
from downloader import download_image


def get_nasa_images(nasa_key, count_images):
    Path("image").mkdir(parents=True, exist_ok=True)
    payload = {
        'api_key': f'{nasa_key}',
        'count': count_images
    }
    url_api_nasa = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url_api_nasa, params=payload)
    response.raise_for_status()
    for apod_number, apod in enumerate(response.json()):
        if apod['media_type'] in 'image':
            urlstring = apod['url']
            path = os.path.join('image', f'nasa_apod_{apod_number}{get_extension(urlstring)}')
            download_image(urlstring, path)


def createParser ():
    parser = argparse.ArgumentParser(description='Downloader APOD images from NASA')
    parser.add_argument ('-c', '--count', default=1, type=int, help='Count images from NASA to download. Default download 1 image.')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    nasa_api_key = os.environ['NASA_API']
    get_nasa_images(nasa_api_key, namespace.count)


if __name__ == '__main__':
    main()
