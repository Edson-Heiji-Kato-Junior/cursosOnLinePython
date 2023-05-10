from builtins import print

from cliente import Cliente, Conta_Bancaria


katojunior = Cliente('Edson Heiji Kato Junior', '282.644.888-97', 44)
dadosfin = Conta_Bancaria(3502, '769656742-0', 2000, 0)

try:
    print('nome:' ,katojunior.nome, 'cpf:',katojunior.cpf, katojunior.idade, 'anos', 'ag: ',dadosfin.agencia, 'CC: ', dadosfin.conta, 'Limite: ',dadosfin.limite, 'Saldo: ',dadosfin.saldo)
    print('Saque....: ',dadosfin.operacao_bancaria('sacar',50.555), '        ==> Saldo do dia: ', dadosfin.saldo)
    print('consultar: ',dadosfin.operacao_bancaria('consultar',500), '           ==> Saldo do dia: ', dadosfin.saldo)
    print('depositar: ',dadosfin.operacao_bancaria('depositar',10500.55), '        ==> Saldo do dia: ', dadosfin.saldo)
    print('Saque....: ',dadosfin.operacao_bancaria('sacar',500), '        ==> Saldo do dia: ', dadosfin.saldo)
except Exception as erro:
    print(erro)