import requests
from django.shortcuts import render
import json

# https://api.via-dolorosa.ru/rc/1/full_info
from requests import HTTPError


def index(request):
    return render(request, 'mainapp/index.html')


def req1(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        response.raise_for_status()
        jsons = response.json()
        response_full.raise_for_status()
        jsons_full = response_full.json()
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
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req1.html', context)


def req2(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90452/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90452/full_info')
        response.raise_for_status()
        jsons = response.json()
        response_full.raise_for_status()
        jsons_full = response_full.json()
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
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req2.html', context)
