numero_de_convidados = input('Digite o numero de convidado: ')
lista_convidados = []
for i in range(int(numero_de_convidados)):
    convidado = input('Convidado - ' + str(i) + ': ')
    lista_convidados.append(convidado)
print(lista_convidados)
