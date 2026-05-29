# Cria um tupla com dez números inteiros.
# mostra o maior, menor e a soma entre eles
# verifica se um número digitado está dentro da tupla e mostra o índice

from random import randint
 
num =  tuple(randint(0,10) for c in range(10)) 
numero_digitado = int(input('Informe um número (entre 0 e 10): '))

if numero_digitado in num:
    print(f'Número digitado {numero_digitado} está na posicão {num.index(numero_digitado)}')
else:
    print('O número não esta na tupla')

print(f'\nMaior número foi {max(num)}')
print(f'Menor número foi {min(num)}')
print(f'Soma de todos eles foram {sum(num)}')
