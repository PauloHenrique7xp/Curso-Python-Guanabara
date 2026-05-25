# DESAFIO 55:
# Faça um programa que leia o peso de cinco pessoas
# e mostre qual foi o maior e o menor peso lidos.

maior = 0  # variável para guardar o maior peso
menor = 0  

for i in range(1, 6):  # laço para 5 pessoas
    peso = float(input(f'Digite o peso da {i}ª pessoa (Kg): '))
    if i == 1:  # na primeira leitura, define ambos
        maior = peso
        menor = peso
    else:
        if peso > maior:  # se o peso atual for maior que o guardado
            maior = peso
        if peso < menor:  # se o peso atual for menor que o guardado
            menor = peso

print(f'O maior peso registrado foi {maior}Kg')
print(f'O menor peso registrado foi {menor}Kg')
