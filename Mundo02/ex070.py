# DESAFIO 70:
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deve perguntar se o usuário quer continuar.
# No final, mostre:
# - o total gasto na compra
# - quantos produtos custam mais de R$1000
# - qual é o nome do produto mais barato

total = 0  # soma dos preços
mais1000 = 0  # conta produtos acima de 1000
mais_barato = ''  # nome do produto mais barato
preco_barato = 0  # preço do produto mais barato

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco

    if preco > 1000:
        mais1000 += 1

    if preco_barato == 0 or preco < preco_barato:  # define o mais barato
        preco_barato = preco
        mais_barato = nome

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'Total gasto na compra: R$ {total:.2f}')
print(f'Produtos que custam mais de R$1000: {mais1000}')
print(f'O produto mais barato foi {mais_barato} que custa R$ {preco_barato:.2f}')
