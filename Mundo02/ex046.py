# DESAFIO 46:
# Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre os números.

from time import sleep

print('Preparando a contagem para os fogos...')
for numero in range(10, -1, -1): # para cada número dentro de um raio de 10 a 0
    print(numero) # vai imprimir 10, 9, 8, 7, 6, 5 ....
    sleep(1)    
print('BOMMMMMMMMMMMMMMMMMMMM!!!')                  