import requests
from django.shortcuts import render
import json

# https://api.via-dolorosa.ru/rc/1/full_info
from requests import HTTPError


def index(request):
    global response
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        response.raise_for_status()
        json = response.json()
    except Exception:
        print('NO')

    context = {
        'title': 'главная',
        'response': response,
        'json': json,

    }
    return render(request, 'mainapp/index.html', context)
