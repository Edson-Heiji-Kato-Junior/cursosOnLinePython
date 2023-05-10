from wsgiref.validate import validator

import firebirdsql

conn = firebirdsql.connect(user = 'SYSDBA', password= 'masterkey', database = 'D:\\Sistemas\\InfysK\\Dados\\INFYSK-OLD.FDB', host = 'localhost', charset='ANSI')

cur = conn.cursor()
valores = [('9000', 'TESTE', 'x', 'x')]
cur.executemany("""insert into cfop (cfop, descricao, resumo, observacao) values (?,?,?,?)"""), valores
conn.commit()

'''for x in cur.fetchall():
    print(x)'''