from veiculo import Veiculo
from carro import Carro
                   #marca, modelo, potencia, cor, rodas, tanque
caminhao = Veiculo('Volvo', '13450', '600cv', 'Branco', 6, 550)

print(type(caminhao.rodas))

print(caminhao.marca, caminhao.modelo, caminhao.potencia, caminhao.cor, caminhao.rodas, caminhao.tanque)

carro = Carro('GM', 'Prisma', '1.4cc', 'Prata', 5)
print('carro original*************************************************')
print(carro.marca, carro.modelo, carro.potencia, carro.cor, carro.rodas, carro.tanque)
carro.abastecer_carro(550)
print('carro abastecido***********************************************')
print( carro.tanque)
print('carro abastecido***********************************************')
km = 440
print('Andou', km,'KM')
carro.andou_km(km)
print( carro.tanque)
carro.pintar('Amarelo')
print('carro pintado*************************************************')
print(carro.marca, carro.modelo, carro.potencia, carro.cor, carro.rodas, carro.tanque)








