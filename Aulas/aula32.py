"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
except ValueError:
    print('O número não é inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_user = input('Informe as horas. Ex: 11:43 ')

try:
    hora = int(hora_user[0:2]) 
    if 0 <= hora <= 11:
        print(f'Bom dia! São {hora_user}')
    elif 12 <= hora <= 17:
        print(f'Boa tarde! São {hora_user}')
    elif 18 <= hora <= 23:
        print(f'Boa noite! São {hora_user}')
    else:
        print('Hora inválida. Digite no formato 00:00 com hora de 0 a 23.')
except:
    print('Formato inválido. Digite no formato 00:00')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Informe seu primeiro nome: ')
verificar = len(nome)

if verificar <= 4:
    print('Seu nome é curto')
elif verificar <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
