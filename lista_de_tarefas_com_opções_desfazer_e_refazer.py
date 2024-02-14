
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

lista = []
historico_desfeito = []


# Inseri primeiramente os comando:
while True:
    print ('Comandos : listar, desfazer ou refazer')
    opcao = (input(f'Digite uma tarefa ou um comando: '))
    print ()

##########################################################
   
# Se o usuario selecionar - listar:
   
    if opcao == 'listar':
        if len(lista) == 0:
            print ('Nao ha nada para listar')

        print ('TAREFAS:\n', lista)
        print ()

###########################################################
   
# Se o usuario selecionar - desfazer:
   
    elif opcao == 'desfazer':

        if len(lista) == 0:
            print ('Nao ha produtos a serem desfeitos')
            print ()
        
        else:
            item_removido = lista.pop() # pop = apaga o ultimo item da lista.
            historico_desfeito.append (item_removido) # vai armazenar o ultimo item removido da lista.

        print (f'Voce deletou da lista o item: {item_removido}')
        print ()

        print ('TAREFAS:\n', lista)
        print ()
            
###########################################################
   
# Se o usuario selecionar - refazer:
   
    elif opcao == 'refazer' :
        if len (historico_desfeito) > 0: # se houver algo para ser refeito. 
            item_refeito = historico_desfeito.pop () # o item_refeito vai apagar o ultimo item adicionado ao historico_desfeito
            lista.append (item_refeito) # e adicionar esse item na lista.
            

        else:
            print ('Nao ha acoes para refazer')
            print ()

        print (f'Voce inseriu na lista o item: {item_refeito}')
        print ()
        print ('TAREFAS:\n', lista)
        print ()
        
###########################################################

    elif opcao == 'sair':
        break

###########################################################
    else:
        lista.append(opcao)
        print ('TAREFAS:\n', lista)
        print ()
        
###########################################################

    with open ('aula119_1_tarefa.json', 'w+', encoding = 'utf8') as arquivo:
        json.dump(
            lista,
            arquivo,
            ensure_ascii = False,
            indent = 2
            )