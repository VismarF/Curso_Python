"""

and= e
Exercício
peça ao usuario para digitar o seu nome
peça ao usuario para digitar sua idade
se o nome e idade forem digitados:
    exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade;
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome é: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é:{nome}')
    print(f'Seu nome invertido é:{nome[::-1]}')
    
    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é:{nome[0]}')
    print(f'A ultima letra do seu nome é:{nome[-1]}')
else:
    print("Desculpe você deixou campos vazioos.")

