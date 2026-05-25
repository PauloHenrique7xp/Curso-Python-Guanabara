# DESAFIO 45:
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

opcoes = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2) # entre 0 1 2 

print('''Escolha sua jogada:
[0] Pedra
[1] Papel
[2] Tesoura''')
usuario = int(input('Digite sua escolha: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(f'Computador escolheu {opcoes[pc]}')
print(f'Você escolheu {opcoes[usuario]}')

if pc == usuario: # se pc for iqual o usuario
    print('Resultado: EMPATE')
elif (pc == 0 and usuario == 1) or (pc == 1 and usuario == 2) or (pc == 2 and usuario == 0): # resultados que mostra que o usuario venceu
    print('Resultado: VOCÊ VENCEU!')
else: 
    print('Resultado: COMPUTADOR VENCEU!')
