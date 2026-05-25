# DESAFIO 50:
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.

soma_pares = 0
quantidade = 0

for i in range(1, 7):  # para cada i dentro de um raio de 1 a 7 que vai de 1 a 6 
    numero = int(input(f'Digite o {i}º número: ')) # faz essa pergunta 6 vezes (está dentro do for)
    if numero % 2 == 0:  # verifica se é par
        soma_pares += numero  # acumula na soma
        quantidade += 1                       

print(f'Você informou {quantidade} números pares e a soma deles é {soma_pares}')
