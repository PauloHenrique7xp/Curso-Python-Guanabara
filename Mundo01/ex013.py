# DESAFIO:
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento 15%

salário = float(input('Informe seu salário R$'))

# salario dividido por 15% depois adiciona o total + o desconto 
aumento = salário + (salário * 15/100)

print(f'Com o salário de R${salário} o funcionário recebeu um aumento de 15% ficando com R${aumento}')