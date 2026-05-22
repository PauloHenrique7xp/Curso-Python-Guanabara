# DESAFIO:
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
# e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da viagem em km? '))

if distancia <= 200: # se distancia for menor ou iqual a 200: BLOCO A
    preco = distancia * 0.50 # BLOCO A 
else: # se não BLOCO B
    preco = distancia * 0.45 # BLOCO B

print(f'O preço da passagem será R${preco:.2f}')
