# DESAFIO 65:
# Crie um programa que leia vários números.
# O programa deve mostrar a média entre eles,
# o maior e o menor valor digitado.
# O usuário decide se continua ou não.

soma = 0  # soma dos números
contador = 0  # quantidade de números
maior = 0  # maior valor
menor = 0  # menor valor

continuar = 'S'  # começa com sim

while continuar == 'S':  # repete enquanto usuário quiser
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:  # primeiro número define maior e menor
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

media = soma / contador  # calcula média

print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
