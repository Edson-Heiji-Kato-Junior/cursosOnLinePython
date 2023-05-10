import oauth2
import json
import urllib.parse


consumer_key = '6ey9Wn4UD7WtJ8t6nyyMZCz9h'
consumer_secret = 'vY8b5JrtvaKbcwfYchEpSs5Xp0NKmQGVvltxDo6mCUAHaYQMJL'

token_key = '1587462337468022792-e8Lf76id9wszmI9W30FOZMP2GwcMwo'
token_secret = 'jn0SXJNhXOFdDXaZoEggt6MUvEM9SxNDVglCmO9BtNFAW'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Novo tweet: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

print(objeto)
