# DESAFIO:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora 
# de se alistar ou se já passou do tempo do alistamento.
# - Mostra o tempo que falta
# - Mostra quanto tempo passou

from datetime import date

ano_nascimento = int(input('Informe o ano do seu nascimento: '))
                     
data_atual = date.today().year # pega a data do seu pc

idade = data_atual - ano_nascimento # soma da idade

if idade == 18: # se idade for iqual a 18
    print(f'hora de se alistar')
elif idade > 18: # se idade for maior
    tempo = idade - 18
    print(f'Passou do prazo de alistamento de {tempo} anos')
else: # unica opção e se a idade for menor
     tempo = 18 - idade
     print(f'Ainda e menor de idade, faltam {tempo} anos para alistamento')