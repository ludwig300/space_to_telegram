# Space to telegram

## This is an assistant for publishing images in telegram, it can:
- Download images from API SpaceX and NASA
- Publish images in telegram

## Installing required dependencies

- [Generate API Key](https://api.nasa.gov/#signUp) for download images from APOD NASA and EPIC NASA.

- [Create new bot in Telegram](https://t.me/BotFather). Use `/newbot`

  `TOKEN` — Type of token. Look like this `5302287822:AAXiCHSBn0xrUOyqee-TeiJ3SQoBd7RkeL8`

- Add bot to channel with admin roots.

## Setting environment variables
* Create `.env` file in project directory and write:
```
NASA_API = Your API Key
TOKEN = Your token
```		
### Requirements
* APScheduler==3.6.3
* certifi==2022.6.15
* cffi==1.15.1
* charset-normalizer==2.1.0
* cryptography==37.0.4
* decorator==5.1.1
* idna==3.3
* pycparser==2.21
* python-dotenv==0.20.0
* python-telegram-bot==13.0
* pytz==2022.1
* pytz-deprecation-shim==0.1.0.post0
* requests==2.28.1
* six==1.16.0
* tornado==6.2
* tzdata==2022.1
* tzlocal==4.2
* urllib3==1.26.10

     
Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```		
## Application launch

### Open project directory from cmd

#### Download images from API SpaceX: 
```
$ python fetch_spacex_images.py -i <id>
```
You can look image `<id>` [here](https://api.spacexdata.com/v5/launches).
This is an optional argument, default it the photo from the last rocket launch will be downloaded.
	
#### Download images from APOD NASA:
```
$ python get_apod_nasa_images.py -c <COUNT>
```
Enter the `<COUNT>` of images to download (default 1).

#### Download EPIC from NASA:
```
$ python get_epic.py
```
This script download 5 EPIC. 

#### Posting image to telegram:
```
$ python posting_image.py <CHAT_ID> -f <FILE>
```
- Positional argument `<CHAT_ID>` - it's ID Telegram chanal or chat, look like this `@testchanal0`
- `<FILE>` - Specify the path to the file. Default publication random file from "./image"

#### Auto posting images to telegram:
```
$ python posting_images_auto.py <CHAT_ID> -t <TIMER> 
```
Publication image from dir `'./image'` 

- Positional argument `<CHAT_ID>` - it's ID Telegram chanal or chat, look like this `@testchanal0`

- `<TIMER>` - Specify the time interval in secs between publications, default 4 hours (14400 secs)

*Project Goals*
	
*Make blogging life easier*