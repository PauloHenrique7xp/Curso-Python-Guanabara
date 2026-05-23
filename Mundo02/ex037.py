# DESAFIO:
# Escreva um programa que leia um número qualquer e peça para o usúario escolhe
# qual será a base da conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Informe um número qualquer: '))

print('ESCOLHA A CONVERSÃO: [1] BINÁRIO [2] OCTAL [3] HEXADECIMAL')

escolha = int(input('Informe o número da escolha: '))

if escolha == 1: # escolha opcão 1
    print(f'Conversão para binário é {bin(num)}')
elif escolha == 2: 
    print(f'Conversão para octal é {oct(num)}')
elif escolha == 3:
    print(f'Conversão para hexadecimal é {hex(num)}')
else: # se ele escolheu uma opção que nao está entre a escolha
    print('Opções inválida')