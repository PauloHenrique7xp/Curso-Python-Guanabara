# DESAFIO:
# Crie um programa que leia o cateto oposto e o cateto adjacente de um triângulo retângulo
# e mostre o comprimento da hipotenusa.

from math import hypot # função que calcula direto a hipotenusa

# lendo os catetos
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

# a função hypot já faz a conta da raiz quadrada da soma dos quadrados
hip = hypot(co, ca)

print(f'A hipotenusa vai medir {hip:.2f}')
