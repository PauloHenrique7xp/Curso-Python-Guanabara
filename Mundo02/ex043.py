# DESAFIO 43:
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: peso ideal
# - entre 25 e 30: sobrepeso
# - entre 30 e 40: obesidade
# - acima de 40: obesidade mórbida

peso = float(input('Qual é o seu peso? (Kg) '))   
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)# calcula o IMC (peso dividido pela altura ao quadrado)

print(f'Seu IMC é {imc:.1f}')  # mostra o valor do IMC com 1 casa decimal

if imc < 18.5:                                   
    print('Você está ABAIXO DO PESO')         
elif 18.5 <= imc < 25:   # peso entre 1 e 3                      
    print('Você está no PESO IDEAL')           
elif 25 <= imc < 30:                              
    print('Você está com SOBREPESO')            
elif 30 <= imc < 40:                             
    print('Você está com OBESIDADE')            
else:                                           
    print('Você está com OBESIDADE MÓRBIDA')  # imprime obesidade mórbida
