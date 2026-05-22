# DESAFIO:
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# regra do triângulo:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # para forma um triângulo 1 lado precisa ser menor que a soma entre 2
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
