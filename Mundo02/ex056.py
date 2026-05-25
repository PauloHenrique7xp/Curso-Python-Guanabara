# DESAFIO 56:
# Programa que lê nome, idade e sexo de 4 pessoas
# No final mostra: média de idade, homem mais velho e quantas mulheres < 20 anos

soma_idades = 0  # guarda a soma das idades
homem_mais_velho = ''  # nome do homem mais velho
idade_homem_mais_velho = 0  # idade do homem mais velho
mulheres_jovens = 0  # conta mulheres com menos de 20

for i in range(1, 5):  # repete 4 vezes
    nome = str(input(f'Nome da {i}ª pessoa: ')).strip()
    idade = int(input(f'Idade da {i}ª pessoa: '))
    sexo = str(input(f'Sexo da {i}ª pessoa [M/F]: ')).strip().upper()

    soma_idades += idade  # soma as idades

    if sexo == 'M' and idade > idade_homem_mais_velho:  # se for homem e mais velho
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo == 'F' and idade < 20:  # se for mulher e menor de 20
        mulheres_jovens += 1

media = soma_idades / 4  # calcula média

print(f'A média de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos')
print(f'Total de mulheres com menos de 20 anos: {mulheres_jovens}')
