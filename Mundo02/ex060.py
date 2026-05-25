# DESAFIO 60:
# Faça um programa que leia um número qualquer
# e mostre o seu fatorial.

num = int(input('Digite um número para calcular o fatorial: '))
resultado = 1  # começa com 1 porque é o neutro da multiplicação
contador = num  # variável auxiliar para ir diminuindo

while contador > 0:  # repete até chegar em 1
    resultado *= contador  # multiplica pelo valor atual
    contador -= 1  # diminui 1 a cada passo

print(f'O fatorial de {num} é {resultado}')
