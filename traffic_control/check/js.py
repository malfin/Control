import base64
import json

import requests

import time

import requests
from requests.exceptions import HTTPError
list_rc = [
    'https://api.via-dolorosa.ru/rc/90451/full_info',
    'https://api.via-dolorosa.ru/rc/90452/full_info',
    'https://api.via-dolorosa.ru/rc/90453/full_info',
    'https://api.via-dolorosa.ru/rc/90454/full_info',
    'https://api.via-dolorosa.ru/rc/90455/full_info',
    'https://api.via-dolorosa.ru/rc/90456/full_info',
    'https://api.via-dolorosa.ru/rc/90457/full_info',
    'https://api.via-dolorosa.ru/rc/90458/full_info',
    'https://api.via-dolorosa.ru/rc/90459/full_info',
    'https://api.via-dolorosa.ru/rc/90460/full_info',
           ]
while True:
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        print(jsonResponse)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# while True:
#     time.sleep(5)
#     a = requests.get('https://api.via-dolorosa.ru/rc/90459/full_info')
#
#     print(a)


# with open('urs.json') as jsonfile:
#     data = json.load(jsonfile)
#     datastr = json.dumps(data)
#     print(datastr)
#     encoded = base64.b64encode(datastr.encode('utf-8'))  # 1 way
#     print(encoded)
