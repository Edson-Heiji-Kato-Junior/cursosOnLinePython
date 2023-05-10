import sys

argumento = sys.argv


def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumento[1] == 'soma':
    result = (float(argumento[2]) + float(argumento[3]))

if argumento[1] == 'sub':
    result = (float(argumento[2]) - float(argumento[3]))

print(result)