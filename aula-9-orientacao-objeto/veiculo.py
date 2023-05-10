#classe é que descreve o objeto
#objeto é criado do instanciamento das classes

class Veiculo:
    def __init__(self, marca, modelo, potencia, cor, rodas, tanque):    #init => metod construtor
        self.marca    = marca
        self.modelo   = modelo
        self.potencia = potencia
        self.cor      = cor
        self.rodas    = rodas
        self.tanque   = tanque

    def abastecer(self, litros):
        self.tanque += litros

    def pintar(self,cor):
        self.cor = cor

    def andou_km(self,km_rodado):
        km_rodado = km_rodado/8
        self.tanque -= km_rodado

