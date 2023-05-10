import datetime
import requests
import json
import re
from datetime import date

def fnc_get_valor_dolar (data_ini= date, data_final = date , moeda = '', tipo_consulta= int):
    #tipo_consulta 1 - Valor Atual / 2 - Valor Periodo /
    #str_data_ini = '{}{}{}'.format(data_ini.year, data_ini.month,data_ini.day)
    #str_data_fim = '{}{}{}'.format(data_final.year, data_final.month,data_final.day)
    if tipo_consulta == 1:
        requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/'+moeda)
    elif tipo_consulta == 2:
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/daily/'+moeda+'/?start_date='+str_data_ini+'&end_date='+str_data_fim)
    requisicao_dic = json.loads(requisicao.text)
    return requisicao_dic

def fnc_imprime_resultado(requisicao_dic, moeda):
    print(requisicao_dic[''+moeda+'']['code'],'-',requisicao_dic[''+moeda+'']['codein'])
    print(requisicao_dic[''+moeda+'']['name'])
    print('Cotação Maxima: ', requisicao_dic[''+moeda+'']['high'], '/','Cotação Mínima: ', requisicao_dic[''+moeda+'']['low'])
    print('Variação......: ',requisicao_dic[''+moeda+'']['varBid'],'/','Porcentagem: ', requisicao_dic[''+moeda+'']['pctChange'],'%')
    print('Compra........: ',requisicao_dic[''+moeda+'']['bid'],   '/','Venda: ', requisicao_dic[''+moeda+'']['ask'])
    print('Data: ',requisicao_dic[''+moeda+'']['create_date'])

sair = False
data_ini = date
data_fim = date
while not sair:
    print('1-USD-BRL -> Dolar\n2-EUR-BRL -> Euro \n3-BTC-BRL -> Bitcoin \n4-SAIR \nDigite o número referente a Moeda: ')
    opcao = input()
    if opcao == '4':
        sair = True
    else:
        data_ini = input(datetime.date)
        data_fim = input(datetime.date)
        print(data_ini)
        match opcao:
            case '1':
                moeda = 'USD-BRL'
                moeda_imp = 'USDBRL'
            case '2':
                moeda = 'EUR-BRL'
                moeda_imp = 'EURBRL'
            case '3':
                moeda = 'BTC-BRL'
                moeda_imp = 'BTCBRL'
        req = fnc_get_valor_dolar(data_ini, data_fim, moeda, 1)
        fnc_imprime_resultado(req, moeda_imp)

