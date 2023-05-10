minha_lista    = ['oi', 'lista', 1 , 'teste']
#lista tem indice, pode adicionar, substituir, removerpoder ser vazia, tamanho infinito

minha_tupla    = ('tupla', 'usa', 'parentese', 'tamanho fixo')
#tamanho fixo, só é possivel alterar o valor,
# não tem como adicionar/remover novos intem (não tem append / remove) possue indice
# => tuple

meu_dicionario = {'dicionario': 'usa chave para inicializar ', 'nome': 'Dinho', 'idade': 44}
# dicionario chave e valor, => dict

meu_conjunto   = {'dinho', 'edson' }
# pode adicionar/remover, não tem indice, so tem valor dentro dele. não existe valores repetidos, pode adicionar itens
# tamanho infinito, pode adicionar e remover itens => set


print(minha_lista[0])
print(type(minha_lista))
print('***********************************************************************************')
print(minha_tupla)
print(type(minha_tupla))
print(minha_tupla[0])

cont = 0
for x in minha_tupla:
    print('for:',cont, x)
    cont += 1

# para alterar os valores da tupla, deve-se altera-la por inteiro (sempre respeitado o tamanho) ex:
minha_tupla = ('novo', 'valor', 1, 2)
print(minha_tupla)


if 1 in minha_tupla:
    print('if 1 in minha_tupla =>',1)

print('***********************************************************************************')
#dicionario é usado para busca, pois é muito mais eficiente que a lista.
print(meu_dicionario)

print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
print('len(meu_dicionario)',len(meu_dicionario))
if 'Dinho' in meu_dicionario.values():
    print('if Dinho in meu_dicionario.values()')

for x in meu_dicionario.values():
    print(x)

meu_dicionario['idade'] = 20/2
meu_dicionario['novo_campo'] = 'adicionado'
print(meu_dicionario)

print('***********************************************************************************')
# quando for pesquisar um volume de dados muito grande usar lista
# pesquisa no metodo informacao in meu_conjunto
print(meu_conjunto)
meu_conjunto.add('novo_nome')
if 'novo_nome' in meu_conjunto:
    print('if ''novo_nome'' in meu_conjunto', meu_conjunto)
meu_conjunto.remove('novo_nome' and 'dinho')
print(meu_conjunto)

meu_conjunto_teste = set()
x = 0
while x < 1000:
    print(x)
    meu_conjunto_teste.add(x)
    x += 1
if 741 in meu_conjunto_teste:
    print('741')



