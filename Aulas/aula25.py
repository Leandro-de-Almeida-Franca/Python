# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Leandro'
preco = 10000.433543
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (15, 13))