# DESAFIO:
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final uma mensagem 
# de acordo com sua média.
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Informe primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

média = (nota1 + nota2) / 2
print(f'Com nota {nota1} e {nota2} sua média é {média}')

if média >= 7: # se média for maior ou iqual
    print('Aluno aprovado')
elif 5 <= média < 6.9: # média entre 5 e 6.9
    print('Aluno de recuperação')
else: # abaixo de 5
    print('Aluno reprovado')