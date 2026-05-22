# DESAFIO:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar. Sabendo
# que o carro cust R$60 por dia e R$0.15 por Km rodado

Km_rodado = float(input('Informe a quantidade de Km percorrido: '))
dias_alugado = int(input('Informe a quantidade de dias: '))

# calcula o dias por 60 e km por 0.15
custo = (dias_alugado * 60) + (Km_rodado * 0.15)

print(f'O total do custo do carro foi de R${custo:.2f}')