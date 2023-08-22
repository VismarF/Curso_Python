"""
Exercicio guiado com while
Iterando strings com while
"""
#       0123456789101112
nome = 'Maria Eduarda' #string são interaveis

indice = 0
while indice < len(nome):#equanto o indice for menor que o numero de caracter do nome ele estara em Loop
    print(f'{nome[indice]}',end='*')#função end=''é responsável por alterar esse comportamento, possibilitando ao desenvolvedor trocar qual caracter será adicionado ao final do dado impresso no terminal
    indice += 1