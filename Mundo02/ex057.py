# DESAFIO 57:
# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()  # lê e já coloca em maiúsculas

while sexo not in 'MF':  # enquanto não for M ou F
    sexo = str(input('Valor inválido. Digite novamente [M/F]: ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')  # mostra resultado final
