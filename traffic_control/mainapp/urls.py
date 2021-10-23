from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('req1', mainapp.req1, name='req1'),
    path('req2', mainapp.req2, name='req2'),
]
