# DESAFIO 69:
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deve perguntar se quer continuar.
# No final, mostre:
# - quantas pessoas têm mais de 18 anos
# - quantos homens foram cadastrados
# - quantas mulheres têm menos de 20 anos

maiores18 = 0  # conta pessoas com mais de 18
homens = 0     # conta homens
mulheres_menos20 = 0  # conta mulheres com menos de 20

while True:  # laço infinito até o usuário parar
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if idade > 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiores18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos20}')
