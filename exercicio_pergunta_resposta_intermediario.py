
# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0 # contabilizando os acertos . 
for pergunta in perguntas: # cria um indicador . 
    print('Pergunta:', pergunta['Pergunta']) # printar Pergunta, onde = Perguntas, no campo Pergunta.
    print()

#########################################################################################################

    opcoes = pergunta['Opções'] # Defini Opcoes . 
    for i, opcao in enumerate(opcoes): # Cria uma iteração enumerando as opcoes de resposta . 
        print(f'{i})', opcao) # estrutura para apresentar o valor em tela. 
    print()

#########################################################################################################

    escolha = input('Escolha uma opção: ') # Para o usuario responder . 

#########################################################################################################

    acertou = False # variavel, que sera utilizada no IF abaixo.  
    escolha_int = None # variavel, que sera utilizada no IF abaixo.  
    qtd_opcoes = len(opcoes) 

    if escolha.isdigit(): 
        escolha_int = int(escolha) # se numero digitado for inteiro - Transformacao. 

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']: # se a opcao selecionada pelo usuario for igual resposta.
                acertou = True

#########################################################################################################

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

############################################################################################################

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')