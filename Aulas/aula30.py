"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""

velocidade = 61 # Velocidade atual do carro
local_carro = 90 #Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está 
RADAR_RANGE = 1 # A distância onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1
multar_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if multar_carro and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')