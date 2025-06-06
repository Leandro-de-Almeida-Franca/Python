n1 = input('Digite um valor> ')
n2 = input('Digete outro valor: ')

if n1 > n2:
    print(f'O {n1=} é maior do que o {n2=}')
elif n2 > n1:
    print(f'O {n2=} é maior do que o {n1=}')
elif n1 == n2:
    print(f'O valor de {n1=} e {n2=} são iguais')
else:
    print('Erro!')