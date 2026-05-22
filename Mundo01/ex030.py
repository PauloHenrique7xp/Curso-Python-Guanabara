# DESAFIO:
# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))

if num % 2 == 0: # se a divisão de um número tive resto iqual a 0: BLOCO A
    print(f'O número {num} é PAR') # BLOCO A
else: # se não BLOCO B
    print(f'O número {num} é ÍMPAR') # BLOCO B
