import base64
import json

with open('urs.json') as jsonfile:
    data = json.load(jsonfile)
    datastr = json.dumps(data)
    print(datastr)
    encoded = base64.b64encode(datastr.encode('utf-8'))  # 1 way
    print(encoded)
