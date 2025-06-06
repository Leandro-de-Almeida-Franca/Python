# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Digite a senha: ')

if not senha:
    print('Você não digitou nada')

print(not True)
print(not False)