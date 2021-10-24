import requests
from django.shortcuts import render
import json

# https://api.via-dolorosa.ru/rc/1/full_info
from requests import HTTPError


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def req1(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req1.html', context)


def req2(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req2.html', context)


def req3(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req3.html', context)


def req4(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req4.html', context)


def req5(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req5.html', context)


def req6(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req6.html', context)


def req7(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req7.html', context)


def req8(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req8.html', context)


def req9(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req9.html', context)


def req10(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90451/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90451/full_info')
        if response.status_code == 200:
            response.raise_for_status()
            jsons = response.json()
            phase_id = jsons['current_phase_id']
            # print(phase_id)
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
            if response_full.status_code == 200:
                response_full.raise_for_status()
                jsons_full = response_full.json()
            else:
                jsons_full = 'Ошибка на сервере 500/502'
        else:
            jsons_full = 'Ошибка на сервере статус 500/502'
            jsons = 'Ошибка на сервере 500/502'
            s1 = []
    except Exception:
        print('NO')

    context = {
        'title': 'req1',
        # 'text': text,
        'jsons_full': jsons_full,
        'json': jsons,
        's1': s1,

    }
    return render(request, 'mainapp/req10.html', context)
