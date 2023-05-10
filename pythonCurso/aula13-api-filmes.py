import requests
import json

def print_filme (dados_filme):
    print('Título.............:', dados_filme['Title'])
    print('Ano................:',dados_filme['Year'])
    print('Avaliado...........:',dados_filme['Rated'])
    print('Lançado............:',dados_filme['Released'])
    print('Tempo.............:',dados_filme['Runtime'])
    print('Genero............:',dados_filme['Genre'])
    print('Diretor...........:',dados_filme['Director'])
    print('Escritor..........:',dados_filme['Writer'])
    print('Atores............:',dados_filme['Actors'])
    print('Resumo............:',dados_filme['Plot'])
    print('Idioma............:',dados_filme['Language'])
    print('País..............:',dados_filme['Country'])
    print('Premios...........:',dados_filme['Awards'])
    print('Poster............:',dados_filme['Poster'])
    print('Título............:',dados_filme['Ratings'])
    print('Avaliação.........:',dados_filme['Metascore'])
    print('Tipo..............:',dados_filme['Type'])
    print('DVD...............:',dados_filme['DVD'])
    print('Produção..........:',dados_filme['Production'])
    print('Site..............:',dados_filme['Website'])

def pesquisa_filme():
    busca = input('Digite o nome do filme....: ')
    req = requests.get('http://www.omdbapi.com/?t='+busca+'&apikey=f40215b2')
    dados_filme = json.loads(req.text)
    return dados_filme



rec = None

try:

    dados_filme = pesquisa_filme()
    if dados_filme['Response'] == 'False':
        print('Filme Não Encontrado')
    else:
        print_filme(dados_filme)

except Exception as erro:
    print(erro)
    exit()













