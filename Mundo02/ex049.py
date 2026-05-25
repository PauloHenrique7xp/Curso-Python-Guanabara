# DESAFIO 49:
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite um número para ver sua tabuada: '))

print(f'Tabuada do {numero}:')
for multiplicador in range(1, 11):   # vai de 1 até 10 (for sempre tira - 1)
    resultado = numero * multiplicador 
    print(f'{numero} x {multiplicador} = {resultado}') # ordem de variavel 
