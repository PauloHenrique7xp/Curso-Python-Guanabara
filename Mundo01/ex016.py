# DESAFIO: 
# Crie um programa que leia um número qualquer pelo teclhado e mostre sua porção inteira.

from math import trunc

# um valor que seja  decimal
valor = float(input('Informe um valor qualquer:'))

# observar que a função trunc tem como objetivo retira a parte decimal de um número
print(f'Porção inteira do valor {valor} é {trunc(valor)}')