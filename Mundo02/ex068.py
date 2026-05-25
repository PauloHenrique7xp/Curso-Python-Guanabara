# DESAFIO 68:
# Crie um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas.

from random import randint  # para gerar número aleatório

vitorias = 0  # conta vitórias do jogador

while True:  # laço infinito até o jogador perder
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)  # computador escolhe número
    total = jogador + computador
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}')

    if (total % 2 == 0 and escolha == 'P') or (total % 2 == 1 and escolha == 'I'):
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break

print(f'Fim de jogo! Você conseguiu {vitorias} vitórias consecutivas.')
