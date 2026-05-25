# DESAFIO 53:
# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()  # lê a frase, tira espaços extras e coloca em maiúsculas
palavras = frase.split()  # separa em lista de palavras
junto = ''.join(palavras)  # junta tudo sem espaços
inverso = junto[::-1]  # cria a string invertida

print(f'O inverso de {junto} é {inverso}')  # mostra a comparação

if inverso == junto:  # se a frase invertida for igual à original
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um palíndromo.')
