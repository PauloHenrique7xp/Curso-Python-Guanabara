# DESAFIO:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

# valor decimais(float)
nota1 = float(input('Informe primeira nota: '))
nota2 = float(input('Informe segunda nota: '))

# usamos os parenteses para a ordem de calculo como na matematica
print(f'Média das notas {nota1} e {nota2} é {(nota1 + nota2) / 2}')