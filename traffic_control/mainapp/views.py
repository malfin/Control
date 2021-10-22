import requests
from django.shortcuts import render
import json




# https://api.via-dolorosa.ru/rc/1/full_info
def index(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/1/full_info')
    except Exception:
        print('NO')

    with open('check/urs.json', 'r') as f:
        d = json.load(f)
    context = {
        'title': 'главная',
        'response': response,
        'json': d,
    }
    return render(request, 'mainapp/index.html', context)
