def soma (numero1, numero2):
    resp = numero1 + numero2
    return resp



def tem_sete_letras(paramentro):
    if len(paramentro) == 7:
        return True
    else:
        return False

print(tem_sete_letras('1234567'))

retorno = soma(10.88, 1.89)
print(retorno)

if tem_sete_letras('1234567'):
    print('tem 7 letras mesmo')