# DESAFIO 48:
# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# deve  ter variavel para recebe valores
soma = 0 
contagem = 0

for numero in range(1, 501, 2): # para cada número dentro de um raio de 1 a 501 pulando de 2 em 2 (número pares)
    if numero % 3 == 0:  # se o número divisivel por 3 for iqual a 0 (multiplo de 3)
        soma += numero  # acumulação de soma dos números pares e multiplos                
        contagem += 1  # adiciona + 1 cada vez que acha um número par e multiplo de 3

print(f'A soma dos {contagem} valores encontrados é {soma}') 
