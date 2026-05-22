# DESAFIO:
# Crie um programa que leia quantos dinheiro uma pessoa tem na carteira
# e mostre quantos de Dólares ela pode comprar. 

# reais e um valor decimal por que tem parte quebrada
reais = float(input('Informe quantos tem na carteira: R$'))

# usamos uma variável por causa que não e um valor fixo
cotacao = 5.04

# aqui nos fazemos o calculo sem variável
print(f'Com R${reais} você consegue comprar U${reais / cotacao}')