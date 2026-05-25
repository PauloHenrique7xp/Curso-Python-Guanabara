# DESAFIO 44:
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o preço normal e condições de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Preço das compras: R$ '))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? ')) # aqui a pessoa digita o número escolhido

if opcao == 1: 
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')
else:
    total = preco
    print('Opção inválida de pagamento!')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.') # sempre vai mostra no final
