# DESAFIO 52:
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

valor = int(input('Digite um número inteiro: '))
divisores = 0

for teste in range(1, valor + 1): # aqui pecorre de 1 ate o valor ( + 1 e por causa que o programa sempre tira - 1 )
    if valor % teste == 0:    # verifica se é divisível
        divisores += 1

if divisores == 2:   # primo só tem 2 divisores (1 e ele mesmo)
    print(f'O número {valor} é PRIMO')
else:
    print(f'O número {valor} NÃO é primo')
