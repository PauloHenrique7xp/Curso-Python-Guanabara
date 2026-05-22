# DESAFIO:
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('O nome tem SILVA?', 'SILVA' in nome.upper())
