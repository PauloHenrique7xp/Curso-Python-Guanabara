# DESAFIO:
# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com sua idade:
# ate 9 anos: MIRIM        - até 19 anos:JUNIOR
# até 14 anos: INFATIL     - até 25 anos: sênior      - acima: MASTER

from datetime import date 

ano_nascimento = int(input('Informe o ano de nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} idade')

if idade <= 14: # se idade for menor ou iqual a 14
    print('MIRIM')
elif idade <= 14:
    print('INFATIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else: # unica opção e ser maior que 25
    print('MASTER')