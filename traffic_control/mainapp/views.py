import requests
from django.shortcuts import render
import json

# https://api.via-dolorosa.ru/rc/1/full_info
from requests import HTTPError


def index(request):
    global response
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response.raise_for_status()
        jsons = response.json()
        phase_id = jsons['current_phase_id']
        print(phase_id)
        # if phase_id == 1:

    except Exception:
        print('NO')

    context = {
        'title': 'главная',
        'response': response,
        'json': jsons,

    }
    return render(request, 'mainapp/index.html', context)
