# DESAFIO:
# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

# usando funções do python 
# maior = max(a, b, c)
# menor = min(a, b, c)

# assumimos que  o A e maior e Menor
maior = a
menor = a

if b > maior: # se b for maior que A: BLOCO A
    maior = b # BLOCO A
if b < menor: # se b for menor que A: BLOCO B
    menor = b # bloco B

# mesma logica
if c > maior:
    maior = c
if c < menor:
    menor = c

# aqui que for maior ou menor automaticamente entra an variável maior e menor
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
