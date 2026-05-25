# DESAFIO 71:
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# O programa deve perguntar o valor a ser sacado (inteiro).
# O caixa tem cédulas de R$50, R$20, R$10 e R$1.
# Mostre quantas cédulas de cada valor serão entregues.

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 50  # começa pela maior cédula
total_cedulas = 0

while total > 0:  # enquanto ainda houver valor para sacar
    if total >= cedula:  # se ainda cabe a cédula atual
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:  # mostra quantas cédulas foram usadas
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0  # zera para contar a próxima cédula

print('Saque finalizado. Volte sempre!')
