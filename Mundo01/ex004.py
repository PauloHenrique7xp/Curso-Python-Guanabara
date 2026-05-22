# DESAFIO:
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo.
# e todas as informações possiveis sobre ele

# recebe qualquer coisa no formato de texto(string)
valor = input('Informe alguma coisa: ')

# daqui pra baixo avaliar de que tipo ele é
# exibi True(verdadeiro) or False(falso)
print(f'É número? {valor.isnumeric()}')

print(f'É letra? {valor.isalpha()}')

print(f'É decimal? {valor.isdecimal()}')

print(f'É maiúsculo? {valor.isupper()}')

print(f'É minúsculos {valor.islower()}')

