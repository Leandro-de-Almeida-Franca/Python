# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# L e a n d r o
#-7-6-5-4-3-2-1 

nome = 'Leandro'
print(nome[3])
print(nome[-4])

print('n' in nome)
print('z' in nome)

print('z' not in nome)
print('n' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')