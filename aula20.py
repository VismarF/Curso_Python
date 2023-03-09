# Operadores lógicos
# and(e) or(ou) not(não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer calor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc ja viu)
# 0 0 0 '' false
# também existe o tipo None que é usado para representar um não valor


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    {
        print('Entrada autorizada!!')
    }
else:
    {
        print('Sair!!')
    }