# Operadores lógicos
# and (e) or (ou) not (não)
#or - Qualquer condição verdadeira avalia toda expressoa como verdadeira
#Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
#0 0.0 '' False
#Também existe o tipo None que é usando para representar um não valor

entrada = input('[E]ntrar [S]air> ')
senha_digitada = input('Digite a sua senha: ')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')


#Avaliação de curto circuito
senha = input('Senha: ') or 'Senha Vazia'
print(senha)
print(0 or False or 0 or 'abc' or True)