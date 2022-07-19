import requests
from pathlib import Path
import os
import datetime
from dotenv import load_dotenv
from download_image import download_image


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


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API']
    Path("image").mkdir(parents=True, exist_ok=True)
    get_epic_image(nasa_api_key)
    

if __name__ == '__main__':
    main()
