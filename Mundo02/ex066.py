# DESAFIO 66:
# Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar 999.
# No final, mostre quantos números foram digitados e qual foi a soma deles.
# (sem considerar o flag 999)

soma = 0  # guarda a soma dos números
contador = 0  # conta quantos números foram digitados

while True:  # laço infinito até usar o break
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:  # condição de parada
        break
    soma += num  # soma o número
    contador += 1  # aumenta o contador

print(f'Você digitou {contador} números e a soma deles foi {soma}')
