import json
import pprint

import oauth2
import requests
from setuptools._distutils.command.config import config

consumer_key = '6ey9Wn4UD7WtJ8t6nyyMZCz9h'
consumer_secret = 'vY8b5JrtvaKbcwfYchEpSs5Xp0NKmQGVvltxDo6mCUAHaYQMJL'
token_key = '1587462337468022792-e8Lf76id9wszmI9W30FOZMP2GwcMwo'
token_secret = 'jn0SXJNhXOFdDXaZoEggt6MUvEM9SxNDVglCmO9BtNFAW'

#criando objeto consumidor
consumer = oauth2.Consumer(consumer_key, consumer_secret)

#criando objeto token
api_token = oauth2.Token(token_key,token_secret)

# criando cliente de conexao
cliente = oauth2.Client(consumer,api_token)

requisicao = cliente.request('https://api.twitter.com/2/tweets/text=teste)
print(requisicao)
