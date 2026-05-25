# DESAFIO 64:
# Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar 999.
# No final, mostre quantos números foram digitados e qual foi a soma deles.

soma = 0  # guarda a soma dos números
contador = 0  # conta quantos números foram digitados

num = int(input('Digite um número [999 para parar]: '))
while num != 999:  # repete até digitar 999
    soma += num  # soma o número
    contador += 1  # aumenta o contador
    num = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {contador} números e a soma deles foi {soma}')
