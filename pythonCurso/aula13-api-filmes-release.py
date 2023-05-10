import requests
import json

def print_filmes(dados_filme):
    print('Título.............:',dados_filme['Title'])
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

def pesquisa_filme (filme):
    try:
        result_busca = requests.get('http://www.omdbapi.com/?t='+ filme +'&apikey=f40215b2')
        dicionario = json.loads(result_busca.text)
        if dicionario['Response'] == 'False':
            print('Filme Não Encontrado!!!')
        else:
            return dicionario
    except Exception as erro:
        print(erro)
        return None



sair = False

while not sair:
    filme = input('Digite o Título do Filme ou SAIR: ')
    if filme == 'SAIR':
        sair = True
    else:
        try:
            pesquisa = pesquisa_filme(filme)
            print(pesquisa)
            print_filmes(pesquisa)
        except Exception as erro:
            print(erro)