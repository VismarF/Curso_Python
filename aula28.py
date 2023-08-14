"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    \ significa quebra de linha

uma variavel em letra maiuscula significa q ela é constante e não sera atribuido outros valores a ele
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1
carro_multado_radar_1 =  carro_passou_radar_1 and vel_carro_pass_radar_1
if velocidade < RADAR_1:
    print('Carro não foi multado')
if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')
# if velocidade < RADAR_1 and local_carro < (LOCAL_1 - RADAR_RANGE):
#     print('Carro não foi multado')