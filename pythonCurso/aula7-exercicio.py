def retorna_maior_menor(pLista):
    maior = 0.00
    menor = 0.00
    aux   = 0.00
    for aux in pLista:
        if aux > maior:
            maior = aux
    print('o Maior é: ',maior)
    menor = pLista[0]
    for aux in pLista:
        if aux < menor:
            menor = aux
    print('o Menor é: ',menor)
    quit()

lista = [1321,54564,32465456,2121,455342,45,12,12,5,88,13215,321351651.558,312,21512,51,121,512,1125.444,-1.5644]
print(retorna_maior_menor(lista))