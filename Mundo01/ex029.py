# DESAFIO:
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Qual a velocidade do carro? '))


if velocidade > 80:# se velocidade for maior que 80: BLOCO A
    multa = (velocidade - 80) 
    print(f'Você foi multado! O valor da multa é R${multa:.2f}') # BLOCO A
else: # se não BLOCO B
    print('Tudo certo, você está dentro do limite de velocidade.') # BLOCO B
