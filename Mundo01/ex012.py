# DESAFIO:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Informe o preço de um produto: R$'))

# calcula o preço por 5% e depois retira o preço do 5% com o total
desconto = preço - (preço * 5/100)

print(f'O produto com valor R${preço} Com o desconto de 5% ficou por R${desconto:.2f}')