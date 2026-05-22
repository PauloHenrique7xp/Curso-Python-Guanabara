# DESAFIO:
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido.
# O programa deve escrever na tela se o usuário venceu ou perdeu.

from random import randint # randint função de escolha de número inteiro
from time import sleep # função de tempo 

print('Vou pensar em um número entre 0 e 5...')
num_pc = randint(0, 5)  # sorteia número

palpite = int(input('Qual número você acha que eu pensei? '))

print('Processando...')
sleep(2)  # pausa de 2 segundos 

if palpite == num_pc: # se palpite for iqual a num_pc BLOCO A
    print('Parabéns, você acertou!') # BLOCO A A
else: # se não BLOCO B
    print(f'Errou! o pc pensou no número {num_pc}') # BLOCO B