from random import randint
 
num =  tuple(randint(0,10) for c in range(10)) 
numero_digitado = int(input('Informe um número: '))

if numero_digitado in num:
    print(f'Número digitado {numero_digitado} está na posicão {num.index(numero_digitado)}')
print(f'\nMaior número foi {max(num)}')
print(f'Menor número foi {min(num)}')
print(f'Soma de todos eles foram {sum(num)}')
