# DESAFIO:
# Faça um programa que leia uma frase pelo teclado
# e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

# uma frase sem espaços e com tudo maiúscula
frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece {frase.count("A")} vezes') # count conta quantos 'A' ou qualquer letra tem numa string
print(f'A primeira letra A está na posição {frase.find("A")+1}') # find encontra a primeira posição de uma letra
print(f'A última letra A está na posição {frase.rfind("A")+1}') # rfind encontra a ultima posição

