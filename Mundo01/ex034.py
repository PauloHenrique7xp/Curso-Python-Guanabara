# DESAFIO:
# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do aumento
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250: # se salario for maior que 1250: BLOCO A
    novo = salario + (salario * 0.10)
else: # se não BLOCO B
    novo = salario + (salario * 0.15) 

print(f'O salário era R${salario:.2f} e com aumento passa a ser R${novo:.2f}')
