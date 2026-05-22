# DESAFIO:
# Escreva um programa que leia um valor em metro e a exiba convertido.
# centímetro 
# milímetro

metro = float(input('Informe um valor em metro: '))

# 1 metro = 100cm 
# 1 metro = 1000mm
print(f'Em centímetro {metro * 100} Em milímetro {metro * 1000}')