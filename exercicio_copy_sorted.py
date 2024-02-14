# copy, sorted, produtos.sort

# Exercícios - 1:
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Exercícios - 2:
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Exercícios - 3:
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# Correcao -1 

novos_produtos = copy.deepcopy (produtos)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] *1.1, 2)} # desempacotou produto e definiu que o novo preco seria aumentado em 10%. Round = ajusta as casas decimais, nesse caso 2.
    for produto in produtos # loop para passar preco por preco realizando o reajuste
]
print (*novos_produtos, sep = '\n')

# Correcao -2
def exibir (produtos): #criada uma funcao que ira percorrer toda a lista de produtos
    for i in produtos:
        print (i)

produtos_ordenados_por_nome=sorted(copy.deepcopy (produtos), key = lambda item:item ['nome']) #definido que os produtos seriam ordenados (sorted) pela chave 'nome'.
exibir (produtos_ordenados_por_nome) #chamada a funcao com o parametro definido acima. 

# Correcao -3
def exibir (produtos): #criada uma funcao que ira percorrer toda a lista de produtos
    for i in produtos:
        print (i)

produtos_ordenados_por_nome=sorted(copy.deepcopy (produtos), key = lambda item:item ['preco']) #definido que os produtos seriam ordenados (sorted) pela chave 'preco'.
exibir (produtos_ordenados_por_nome) #chamada a funcao com o parametro definido acima. 