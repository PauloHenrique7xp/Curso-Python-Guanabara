# DESAFIO:
# Faça um programa que leia o nome completo de uma pessoa
# e mostre o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

# separa em partes usando split
partes = nome.split()

print(f'Primeiro nome: {partes[0]}')
print(f'Último nome: {partes[-1]}') # -1 mostra a ultima frase
