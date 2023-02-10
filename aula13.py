#f-strings(formatação de strings)

nome = 'Vismar Flores Choque'
altura = 1.80
peso = 95
imc =  peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)