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

    res = requests.post('https://api.via-dolorosa.ru/rc/90451/custom_phase_program', data=
    {
        "start_phase_id": 3,
        "time_start_sync": 1632402791,
        "t_cycle": 96,
        "phases": [
            {
                "id": 1,
                "t_osn": 31,
                "t_prom": 9,
                "t_min": 4,
                "is_hidden": 'false',
                "directions": 'null'
            },
            {
                "id": 2,
                "t_osn": 13,
                "t_prom": 9,
                "t_min": 4,
                "is_hidden": 'false',
                "directions": 'null'
            },
            {
                "id": 3,
                "t_osn": 25,
                "t_prom": 9,
                "t_min": 15,
                "is_hidden": 'false',
                "directions": 'null'
            }
        ]
    }
                        )
    res.raise_for_status()
    json_post = response.json()
    context = {
        'title': 'главная',
        'response': response,
        'json': json,
        'json_post': json_post,

    }
    return render(request, 'mainapp/index.html', context)
