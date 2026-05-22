# DESAFIO:
# Faça um programa que leia um número inteiro de 0 a 9999
# e mostre na tela cada um dos dígitos separados:
# - unidade, dezena, centena e milhar.

num = input('Digite um número entre 0 e 9999: ')

print(f'Analisando...')
print(f'Unidade: {num[3]}') # aqui apenas usamos para pega a ordem do números
print(f'Dezena : {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar : {num[0]}')