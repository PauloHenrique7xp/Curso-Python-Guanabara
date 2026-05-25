# DESAFIO 58:
# Melhore o jogo do DESAFIO 28 onde o computador "pensa" em um número de 0 a 10
# O jogador deve tentar adivinhar até acertar, mostrando quantos palpites foram necessários.

from random import randint  

computador = randint(0, 10)  # computador escolhe número entre 0 e 10
print('Sou seu computador... pensei em um número entre 0 e 10.')
print('Tente adivinhar!')

acertou = False  # flag para saber se acertou
tentativas = 0   # contador de palpites

while not acertou:  # repete até acertar
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1  # soma mais uma tentativa
    if jogador == computador:  # se acertar
        acertou = True
    else:
        print('Errou... tente novamente!')

print(f'Acertou com {tentativas} tentativas. Parabéns!')
