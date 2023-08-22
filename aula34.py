"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quanfo um codigo não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue##continue pulou o Loop

    if contador >= 10 and contador <= 32:
        continue##continue pulando o Loop dentro do intervalo de 10 a 32

    print(contador)

    if contador == 40: ##Quando o contador chegar ao número 40 ele ira parar o Loop
        break##Ele força a parada do laço

print('Acabou')