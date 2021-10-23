from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('req1', mainapp.req1, name='req1'),
    path('req2', mainapp.req2, name='req2'),
    path('req3', mainapp.req3, name='req3'),
    path('req4', mainapp.req4, name='req4'),
    path('req5', mainapp.req5, name='req5'),
    path('req6', mainapp.req6, name='req6'),
    path('req7', mainapp.req7, name='req7'),
    path('req8', mainapp.req8, name='req8'),
    path('req9', mainapp.req9, name='req9'),
    path('req10', mainapp.req10, name='req10'),
]
