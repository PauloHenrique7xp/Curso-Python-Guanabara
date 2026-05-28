# Exercício 76 - Lista de preços
# Crie uma tupla com produtos e preços e mostre em formato tabulado.

lista_precos = ('Lápis', 1.50, 'Caderno', 12.90, 'Mochila', 89.99, 'Caneta', 2.30)

print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for i in range(0, len(lista_precos), 2):
    produto = lista_precos[i]
    preco = lista_precos[i+1]
    print(f'{produto:.<30} R${preco:>7.2f}')
print('-'*40)

