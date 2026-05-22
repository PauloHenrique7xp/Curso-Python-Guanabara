# DESAFIO:
# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente.

from math import sin, cos, tan, radians # funções de angulos 

angulo = float(input('Digite um ângulo: '))

# precisa converter pra radiano, pq as funções trigonométricas do python usam rad
rad = radians(angulo)

print(f'O seno de {angulo} é {sin(rad):.2f}')
print(f'O coseno de {angulo} é {cos(rad):.2f}')
print(f'A tangente de {angulo} é {tan(rad):.2f}')
