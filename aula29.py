"""
    Flags, is, is not e None

Flag (bandeira) - Marca um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('não passou no if')
if passou_no_if is not None:
    print('Passou no if')
