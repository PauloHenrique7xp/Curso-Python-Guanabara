# DESAFIO:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = input('Informe seu nome completo').strip() # strip serve para retirar os primerios espaços inultil

# .upper deixa tudo em maiúsculo
print(f'Nome em maiúsculo: {nome.upper()}')   
# .lower tudo em minúsculo                
print(f'Nome em minúsculo: {nome.lower()}')
# .replace faz uma troca de string
print(f'Total de letras: {len(nome.replace(' ', ''))}') # trocou os espaços do meio por uma string vazia para nao soma elas

# split faz uma divisição de um texto ex:  paulo/henrique que começa do 0 
primeiro_nome = nome.split[0] # aqui peguei o nome que ta na posição 0 coloquei na variável primeiro_nome
print(f'O primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)}')  