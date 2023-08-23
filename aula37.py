"""
Calculadora com while

#sair = sair.lower()#.lower()ele retorna a mesma string em letras minusculas
#sair = sair.startswith('s')#.startswith(começa com) e .endswith(termina com)
"""
while True:
    opcao = input('Selecione a opção desejada:\nAdição(a)\nSubtração(s)\nMultiplicação(m)\nDivisão(d)\n').lower()
    if opcao == 'a':
        numero_1 = float(input('Informe o primeiro valor: '))
        numero_2 = float(input('Informe o segundo valor: '))

        # if numero_1.isdigit() and numero_2.isdigit():
        #         numero_f1 = float(numero_1)#converte o dado recebido em um numero de ponto flutuante
        #         numero_f2 = float(numero_2)#converte o dado recebido em um numero de ponto flutuante
        print(f'{numero_1} + {numero_2}=',numero_1+numero_2)
        # else:
        #      print('Não um numero')

    elif opcao == 's':
        numero_1 = float(input('Informe o primeiro valor: '))
        numero_2 = float(input('Informe o segundo valor: '))

        # if numero_1.isdigit() and numero_2.isdigit():
        #         numero_f1 = float(numero_1)#converte o dado recebido em um numero de ponto flutuante
        #         numero_f2 = float(numero_2)#converte o dado recebido em um numero de ponto flutuante
        print(f'{numero_1} - {numero_2}=',numero_1 - numero_2)
        # else:
        #      print('Não um numero')

    elif opcao == 'm':
        numero_1 = float(input('Informe o primeiro valor: '))
        numero_2 = float(input('Informe o segundo valor: '))

        # if numero_1.isdigit() and numero_2.isdigit():
        #         numero_f1 = float(numero_1)#converte o dado recebido em um numero de ponto flutuante
        #         numero_f2 = float(numero_2)#converte o dado recebido em um numero de ponto flutuante
        print(f'{numero_1} * {numero_2}=',numero_1 * numero_2)
        # else:
        #      print('Não um numero')

    elif opcao == 'd':
        numero_1 = float(input('Informe o primeiro valor: '))
        numero_2 = float(input('Informe o segundo valor: '))

        # if numero_1.isdigit() and numero_2.isdigit():
        #         numero_f1 = float(numero_1)#converte o dado recebido em um numero de ponto flutuante
        #         numero_f2 = float(numero_2)#converte o dado recebido em um numero de ponto flutuante
        print(f'{numero_1} / {numero_2}=',numero_1 / numero_2)
        # else:
        #      print('Não um numero')
    else:
         print('Opcão informada não existe\nInforme uma opção existente')
                
                
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    