# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x): #criar funcao pede a funcao e X
    def interna(y):#como a funcao externa armazena X, fica pendente o Y
        return funcao(x, y) # isso vai me retornar X,Y
    return interna #e me retornar a funcao interna. 


soma_com_cinco = criar_funcao(soma, 5) # quando eu chamo a variavel (soma_com_cinco) ela aciona a funcao: criar funcao, passando a soma e o valor de X. e eu tenho de indicar sendo assim, apenas Y.
multiplica_por_dez = criar_funcao(multiplica, 10)  # quando eu chamo a variavel (multiplica_por_dez) ela aciona a funcao: criar funcao, passando a multiplica e o valor de X. e eu tenho de indicar sendo assim, apenas Y.

print(soma_com_cinco(10))
print(multiplica_por_dez(10))