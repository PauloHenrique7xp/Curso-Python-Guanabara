# DESAFIO 51:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos da progressão são:')
for termo in range(primeiro, primeiro + razao * 10, razao): # primeiro termo, o limite de 10 vezes e a razão 
    print(termo, end=' → ')
print('Fim')
