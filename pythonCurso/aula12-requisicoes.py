import requests #beautiful soup 4 BS4 => pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}
meus_cookies = {'Ultima-Visita': '10-10-2023'}

dados = {'username': 'katojunior',
      'passaword': '102030'}

texto = None
try:
    requisicao = requests.post('https://putsreq.com/qvwP0NdBoP0SBd6LiapU',
                               headers = cabecalho,
                               cookies = meus_cookies,
                               data = dados)
    texto = requisicao.text
except Exception as e:
    print(e)

print(texto)
