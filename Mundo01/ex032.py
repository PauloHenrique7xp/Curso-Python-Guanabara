# DESAFIO:
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date # importa a função da data 

ano = int(input('Digite um ano (ou 0 para usar o atual): '))

if ano == 0:
    ano = date.today().year  # pega o ano atual do seu pc

# regra do ano bissexto:
# - divisível por 4
# - não divisível por 100, exceto se também for divisível por 400

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # o ano é divisil por 4. Mas não pode ser divisível por 100, execeto se for divisil por 400
    print(f'O ano {ano} é BISSEXTO') # BLOCO A
else: # se não BLCO B
    print(f'O ano {ano} NÃO é bissexto') # BLOCO B
