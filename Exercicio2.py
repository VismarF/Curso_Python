"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Informe um número inteiro:')

if numero.isdigit():
    numero_int = int(numero)
    par = numero_int % 2 == 0
    par_txt = 'ímpar'
    if par:
        par_txt = 'Par'
    
    print(f'O número {numero_int} é {par_txt}')
else:
    print('Você não digitou um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação coletiva. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""