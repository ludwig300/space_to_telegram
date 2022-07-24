import requests
from pathlib import Path
import os
import datetime
from dotenv import load_dotenv
from downloader import download_image
import argparse


def get_epic_image(nasa_api_key, count_images):
    payload = {
        'api_key': f'{nasa_api_key}',
    }
    url_api_epic = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url_api_epic, params=payload)
    response.raise_for_status()
    response_json = response.json()
    for number_epic in range(count_images):
        date = datetime.datetime.fromisoformat(response_json[number_epic]['date'])
        formatted_date = date.strftime("%Y/%m/%d")
        image_name = response_json[number_epic]['image']
        url_template = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_name}.png'
        formatted_response = requests.get(url_template, params=payload)
        formatted_response.raise_for_status()
        path = os.path.join('image', f'{image_name}.png')
        download_image(formatted_response.url, path)


def createParser ():
    parser = argparse.ArgumentParser(description='Downloader APOD images from NASA')
    parser.add_argument ('-c', '--count', default=1, type=int, help='Count images to download. Default download 1 image.')
    return parser


def main():
    load_dotenv()
    parser = createParser()
    namespace = parser.parse_args()
    nasa_api_key = os.environ['NASA_API']
    Path("image").mkdir(parents=True, exist_ok=True)
    get_epic_image(nasa_api_key, namespace.count)


if __name__ == '__main__':
    main()
