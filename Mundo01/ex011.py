# DESAFIO:
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma 
# área de 2m².

larg = float(input('Informe largura: '))
altu = float(input('Informe Altura: '))

# a área é largura multiplicado por altura
área = larg * altu

# se cada 1L tem 2m² para saber quantidade de litros e necessario dividir área por 2
litros = área / 2

print(f'Para pintar uma parede com área de {área}m² e necessario {litros}L de tinta')