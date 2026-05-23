# DESAFIO:
# Escreva um programa que leia dois números e compare-os mostrando na tela uma mensagem
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iquais

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

if num1 > num2: # se o num1 for maior que o num2
    print(f'valor {num1} é maior') # BLOCO A
elif num2 > num1: # ou então o num2 e maior que o número1
    print(f'O valor {num2} é maior') # BLOCO B
else: # unica opção restante e se forem iquais
    print(f'O valor {num1} e {num2} são iquais') # BLOCO C