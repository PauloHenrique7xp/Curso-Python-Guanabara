# DESAFIO:
# Crie um algoritmo que leia um número e mostre o seu doblo, triplo e raiz quadrada.

# valor inteiro(int)
num = int(input('Informe um valor: '))

# calculo baseado na matematica 
# (:.2f) faz com que apôs o ponto apena pegue 2 valores
print(f'Doblo {num * 2} Tripo {num * 3} Raiz quadrada {num ** 0.5:.2f}')