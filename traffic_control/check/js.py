import base64
import json

import requests

import time

import requests

while True:
    time.sleep(5)
    a = requests.get('https://api.via-dolorosa.ru/rc/1/full_info')

    print(a)


# with open('urs.json') as jsonfile:
#     data = json.load(jsonfile)
#     datastr = json.dumps(data)
#     print(datastr)
#     encoded = base64.b64encode(datastr.encode('utf-8'))  # 1 way
#     print(encoded)
