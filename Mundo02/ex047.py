# DESAFIO 47:
# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo de 1 até 50.

print('Números pares entre 1 e 50:')
for valor in range(2, 51, 2):   # começa em 2 e vai de 2 em 2 até 50
    print(valor, end=' ') # end faz os valores recebido irem para direita
print('\nFim da listagem!')
