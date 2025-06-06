"""
Formatação básica de strings
s - string
d - int 
f - float
.<númeors de dígitos>f
x ou X Hecadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:%^10}.')
print(f'{5435.9614897629784698236:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')