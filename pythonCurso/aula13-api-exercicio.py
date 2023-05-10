import json
from builtins import list

import requests
import time


'''
#strutura retornada dicionario {} contendo 3 chaves:
    -Search é uma lista[0..n] contendo de dicionarios (title, year, etc..) 
        Search[0] = > {'Title:'  , 'Year:', ....n}    
        Search[0]['Title'] = matrix
        Search[0]['Year' ] = 2000
        Search[0]['time' ] = 1.53 horas
        Search[1]['Title'] =
        Search[2]['Title'] =
    -totalResults = 'n' (numero de filmes)
    -Response     = 'True' or 'False'
    
    
    
print(filme['Search'])
print(filme['totalResults'])
print(filme['Response'])
'''

'''

def request_filme (filme):
    cont = 1
    response_get = 'True'
    lista_filmes = []
    try:
        while response_get == 'True':
            print('http://www.omdbapi.com/?apikey=f40215b2&s=' + filme + '&page='+str(cont))
            result_request = requests.get('http://www.omdbapi.com/?apikey=f40215b2&s=' + filme + '&page='+str(cont))
            result_dic     = json.loads(result_request.text)
            print_filme(result_dic)
            response_get   = result_dic['Response']
            print_filme(response_get)
            time.sleep(5)
            if response_get == 'False' and cont == 1:
                print('Filme não encontrado!!!')
                return None
            else:
                lista_filmes.append(result_dic['Search'])
                cont += cont
                print(cont,': Filmes Encontrados!')
                return lista_filmes
    except Exception as erro:
        print(erro)

def print_filme (filme):
    cont = 0
    for x in filme:
        print('Título..: ', filme['Search'][cont]['Title' ])
        print('Ano.....: ', filme['Search'][cont]['Year'  ])
        print('Código..: ', filme['Search'][cont]['imdbID'])
        print('Tipo....: ', filme['Search'][cont]['Type'  ])
        print('Poster..: ', filme['Search'][cont]['Poster'])
        print(cont)
        cont += cont

sair = False
while not sair:
    titulo = input('Título ou SAIR: ')
    if titulo == 'SAIR':
        sair = True
    else:
        try:
            lista_filmes = request_filme(titulo)
            if lista_filmes != None:
                print_filme(lista_filmes)
        except Exception as erro:
            print(erro)
'''

def fnc_busca_filme(busca_titulo):
    try:
        lista_filmes = []
        for cont in range(1,101):
            print('Pesquisando no link => http://www.omdbapi.com/?apikey=f40215b2&s=' + busca + '&page=' + str(cont))
            result_busca = requests.get('http://www.omdbapi.com/?apikey=f40215b2&s=' + busca + '&page=' + str(cont))
            result_dic = json.loads(result_busca.text)
            if result_dic['Response'] == 'True':
                for filme in result_dic['Search']:
                    titulo_filme = 'Título: ' + filme['Title']
                    ano_filme    = ' - Ano Lançamento: ' + filme['Year']
                    capa_filme   = ' - Capa: ' + filme['Poster']
                    string       = titulo_filme + ano_filme + capa_filme
                    lista_filmes.append(string)
            else:
                print('Fim da Busca!!')
                break
    except Exception as erro:
        print(erro)
    return lista_filmes

def salvar_arquivo(dados_filme, operacao):
    #operacao => a = append / w = write / r+ = read/write
    if operacao == '1':
        arquivo = open('arquivo.txt', 'w')
    elif operacao == '2':
        arquivo = open('arquivo.txt', 'a')
    cont = 1
    for i in dados_filme:
        arquivo.write(str(cont) + '-' + i +'\n')
        cont = cont +1



sair = False
lista_filmes = []
while not sair:
    cont_filmes = 1
    busca = input('Digite o título do filme ou SAIR: ')
    if busca == 'sair' or busca == 'SAIR' or busca == 'Sair':
        sair = True
    else:
        filmes_localizados = fnc_busca_filme(busca)
        for x in filmes_localizados:
            print(cont_filmes,'-',x)
            cont_filmes = cont_filmes + 1
            #time.sleep(0.1)
        salvar = input('Salvar no arquivo?')
        if salvar == 'sim':
            print('1- Criar Novo Arquivo: ')
            print('2- Adicionar no Arquivo Exixtente: ')
            opcao_salvar = str
            opcao_salvar = input()
            salvar_arquivo(filmes_localizados,opcao_salvar)