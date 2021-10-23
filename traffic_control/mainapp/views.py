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
        response2 = requests.get('https://api.via-dolorosa.ru/rc/90452/status')
        response_full2 = requests.get('https://api.via-dolorosa.ru/rc/90452/full_info')
        response2.raise_for_status()
        jsons2 = response2.json()
        response_full2.raise_for_status()
        jsons_full2 = response_full2.json()
        phase_id2 = jsons2['current_phase_id']
        print(phase_id2)
        s1 = []
        # if phase_id == 1:
        if phase_id2 == 1:
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
        elif phase_id2 == 2:
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
        elif phase_id2 == 3:
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
        'response': response2,
        'jsons_full': jsons_full2,
        'json': jsons2,
        's1': s1,

    }
    return render(request, 'mainapp/req2.html', context)


def req3(request):
    try:
        response3 = requests.get('https://api.via-dolorosa.ru/rc/90453/status')
        response_full3 = requests.get('https://api.via-dolorosa.ru/rc/90453/full_info')
        response3.raise_for_status()
        jsons3 = response3.json()
        response_full3.raise_for_status()
        jsons_full3 = response_full3.json()
        phase_id3 = jsons3['current_phase_id']
        print(phase_id3)
        s1 = []
        # if phase_id == 1:
        if phase_id3 == 1:
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
        elif phase_id3 == 2:
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
        elif phase_id3 == 3:
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
        'response': response3,
        'jsons_full': jsons_full3,
        'json': jsons3,
        's1': s1,

    }
    return render(request, 'mainapp/req3.html', context)


def req4(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90454/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90454/full_info')
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
    return render(request, 'mainapp/req4.html', context)


def req5(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90455/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90455/full_info')
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
    return render(request, 'mainapp/req5.html', context)


def req6(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90456/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90456/full_info')
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
    return render(request, 'mainapp/req6.html', context)


def req7(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90457/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90457/full_info')
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
    return render(request, 'mainapp/req7.html', context)


def req8(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90458/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90458/full_info')
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
    return render(request, 'mainapp/req8.html', context)


def req9(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90459/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90459/full_info')
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
    return render(request, 'mainapp/req9.html', context)


def req10(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/90460/status')
        response_full = requests.get('https://api.via-dolorosa.ru/rc/90460/full_info')
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
    return render(request, 'mainapp/req10.html', context)
