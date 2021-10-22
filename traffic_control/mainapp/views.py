import requests
from django.shortcuts import render


# https://api.via-dolorosa.ru/rc/1/full_info
def index(request):
    try:
        response = requests.get('https://api.via-dolorosa.ru/rc/1/full_info')
    except Exception as err:
        print('NO')
    context = {
        'title': 'главная',
        'response': response,
    }
    return render(request, 'mainapp/index.html', context)
