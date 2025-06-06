# Operadores lógicos
# and (e) or (ou) not (não)
#and - Todas as condições precisam ser verdadeiras
# SEqualquer valor for considerado falso, a expressão interira será avaliada naquele valor
#São considerados false
#0 0.0 '' False
#Também existe o tipo None que é usando para representar um não valor

entrada = input('[E]ntrar [S]air> ')
senha_digitada = input('Digite a sua senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')


#Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)