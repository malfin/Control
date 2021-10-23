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
        s1 = []
        # if phase_id == 1:
        if phase_id == 1:
            s1 = [{
                "id": 1,
                "t_osn": 32,
                "t_prom": 6,
                "t_min": 4,
                "is_hidden": False,
                "directions": [
                    1,
                    2
                ]}]
        elif phase_id == 2:
            s1 = [{
                "id": 2,
                "t_osn": 25,
                "t_prom": 6,
                "t_min": 4,
                "is_hidden": False,
                "directions": [
                    3
                ]
            }]
        elif phase_id == 3:
            s1 = [{
                "id": 3,
                "t_osn": 15,
                "t_prom": 6,
                "t_min": 15,
                "is_hidden": False,
                "directions": [
                    4,
                    5,
                    6
                ]
            }]
        else:
            print('Error')

    except Exception:
        print('NO')

    context = {
        'title': 'главная',
        'response': response,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/index.html', context)
