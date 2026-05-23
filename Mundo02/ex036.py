# DESAFIO:
# Escreva um programa para aprovar o empréstimo bancário para a comprar de uma casa
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# A prestação mensal, não pode exceder 30% do salário

Valo_casa = float(input('Informe o valor da casa: '))
renda_mensal = float(input('Informe sua renda mendal: R$'))
anos = int(input('Em quantos anos voce deseja pagar? '))

prestação = renda_mensal / (anos * 12) # calculamos quantos ele irá  pagar
limite = renda_mensal * 0.3 # aqui colocamos o limite de 30% 

if prestação <= limite: # se prestação for menor ou iqual ao limite: BLOCO A
    print('EMPRESTIMO ACEITO!!') # BLOCO A
else: # se prestação for maior que limite: BLOCO B
    print('EMPRESTIMO NEGADO!!') # BLOCO B