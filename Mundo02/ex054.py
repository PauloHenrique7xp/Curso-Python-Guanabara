# DESAFIO 54:
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas delas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date 
ano_atual = date.today().year  # pega o ano atual

maiores = 0  # contador de maiores de idade
menores = 0  # contador de menores de idade

for i in range(1, 8):  # laço para 7 pessoas
    nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = ano_atual - nascimento  # calcula idade
    if idade >= 18:  # se for maior ou iqual a 18
        maiores += 1
    else:
        menores += 1

print(f'Total de maiores de idade: {maiores}')
print(f'Total de menores de idade: {menores}')
