from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, potencia, cor, tanque):
        Veiculo.__init__(self, marca, modelo, potencia, cor, 4 , tanque)

    def abastecer_carro (self, litros):
        if self.tanque + litros > 50:
            print('vai derramar')