import datetime
import requests
import json
import re
from datetime import date

def fnc_get_clima (cidade = ''):
    requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ cidade + '&lang=pt_br&appid=17761f1d6d9958f8ab9888f9c5b5c84d')
    requisicao_dic = json.loads(requisicao.text)
    return requisicao_dic

def fnc_imprime_resultado(requisicao_dic):
    print('Descrição: ', requisicao_dic['weather'][0]['description'])
    temperatura = float(requisicao_dic['main']['temp'])
    temperatura = (temperatura - 273.15)
    print('Temperatura: ', str(temperatura) + ' Cº')


sair = False
while not sair:
    cidade = input('Digite a cidade ou Sair: ')
    if cidade == 'sair':
        sair = True
    else:
        req = fnc_get_clima(cidade)
        fnc_imprime_resultado(req)



