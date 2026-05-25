# DESAFIO 67:
# Crie um programa que mostre a tabuada de vários números.
# O programa só para quando o usuário digitar um número negativo.

while True:  # laço infinito até usar break
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:  # condição de parada
        break
    print('-' * 30)
    for i in range(1, 11):  # mostra de 1 até 10
        print(f'{num} x {i} = {num*i}')
    print('-' * 30)

print('Programa de tabuada encerrado. Volte sempre!')
