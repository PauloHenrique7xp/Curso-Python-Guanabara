# ler 4 números inteiros e armazená-los em uma tupla.
# motrar:
# Quantas vezes apareceu o número 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares

num = (int(input('Informe o primeiro número: ')),
       int(input('Infomre o outro número: ')),
       int(input('Infomre o outro número: ')),
       int(input('Infomre o outro número: ')))

print(f'Número 9 apareceu {num.count(9)} vezes')
print(f'Posição do primeiro número 3 foi {num.index(3)} posição')
print('Os número pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')