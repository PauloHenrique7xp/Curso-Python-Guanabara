# DESAFIO 59:
# Crie um programa que leia dois valores e mostre um menu:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# O programa deve executar até que o usuário escolha a opção 5.

from time import sleep  # usado para dar pequenas pausas

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0  # guarda a escolha do usuário

while opcao != 5:  # repete até escolher sair
    print('''\nEscolha uma opção:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    opcao = int(input('Sua opção: '))

    if opcao == 1:  # soma
        print(f'A soma de {n1} + {n2} = {n1+n2}')
    elif opcao == 2:  # multiplicação
        print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
    elif opcao == 3:  # maior valor
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print('Os dois valores são iguais')
    elif opcao == 4:  # pedir novos números
        n1 = int(input('Digite o novo primeiro valor: '))
        n2 = int(input('Digite o novo segundo valor: '))
    elif opcao == 5:  # sair
        print('Finalizando...')
    else:
        print('Opção inválida, tente de novo.')
    sleep(1)  # pausa de 1 segundo

print('Programa encerrado. Até logo!')
