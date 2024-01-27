# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

'''

def duplicar (numero):
    return f' O numero duplicado ({numero}) é: {(int(numero)) * 2}'
    
def triplicar (num):
    return f' O numero triplicado ({numero}) é: {(int(numero)) * 3}'
        
def quadruplicar (num):
    return f' O numero triplicado ({numero}) é: {(int(numero)) * 4}'

numero = input ('Digite o numero que gostaria de realizar as Operacoes: ')


print (duplicar(numero))
print (triplicar(numero))
print (quadruplicar(numero))

'''

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):


def criar_multiplicador(multiplicador):# crio uma funcao que vai receber um multiplicador .
    def multiplicar(numero): # dentro da funcao, crio outra funcao que recebe um numero como parametro . 
        return numero * multiplicador # numero * parametro 
    return multiplicar # retorna a funcao . 


duplicar = criar_multiplicador(2) # chamo a funcao acima e passo 1 argumento == multiplicador que ira operar com o numero .
triplicar = criar_multiplicador(3) # chamo a funcao acima e passo 1 argumento == multiplicador que ira operar com o numero .
quadruplicar = criar_multiplicador(4) # chamo a funcao acima e passo 1 argumento == multiplicador que ira operar com o numero .

print(duplicar(2)) # chamo a variavel acima, que chama a funcao e insiro 1 numero que ira operar com o multiplicador .
print(triplicar(2)) # chamo a variavel acima, que chama a funcao e insiro 1 numero que ira operar com o multiplicador .
print(quadruplicar(2))  # chamo a variavel acima, que chama a funcao e insiro 1 numero que ira operar com o multiplicador .