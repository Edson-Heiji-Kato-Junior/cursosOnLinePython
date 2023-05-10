class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome  = nome
        self.cpf   = cpf
        self.idade = idade

class Conta_Bancaria:
    def __init__(self, agencia, conta, limite, saldo):
        self.agencia = agencia
        self.conta   = conta
        self.limite  = limite
        self.saldo   = saldo

    def operacao_bancaria(self, operacao, valor):
        if operacao == 'depositar':
            self.saldo += valor
        elif operacao == 'sacar':
            self.saldo -= valor
        if operacao == 'consultar':
            return ''
        else:
            return(valor)