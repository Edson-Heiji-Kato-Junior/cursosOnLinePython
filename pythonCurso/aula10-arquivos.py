#open('C:\\Users\\Sabrina\\Downloads\\arquivo.txt', 'w')
#open('arquivo.txt', 'r') => read
#open('arquivo.txt', 'w') => write senão exitir ele cria, caso exista ele sobreescreve
#open('arquivo.txt', 'r+') => leitura e escrita
#open('arquivo.txt', 'a') => senao exitir ele cria, abre no modo apende, para adicionar no final do arquivo
#open('arquivo.txt', 'b') => arquivos tipo binario, executavel caso queira ler o arquivo binario usar 'rb' ler binario
arquivo = open('arquivo.txt', 'r+')
print(type(arquivo))
print(arquivo)
for i in range(0,1000):
    arquivo.write('gdfgdfgdfg '+ str(i)+'\n')

for x in arquivo: #lendo arquivo
    print(x)

print(arquivo.read())

