"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios.
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letro do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')