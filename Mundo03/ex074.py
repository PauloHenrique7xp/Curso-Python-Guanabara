# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e tambem indique o menor e o maior valor estão na tupla.
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )

print('Os valores escolhido foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nMaior valor sorteado foi {max(numeros)}')
print(f'Menor valor sorteado foi {min(numeros)}')