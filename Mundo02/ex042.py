# DESAFIO:
# refaça o DESAFIO 35 dos triângulos, acrescentendo o recurso de mostra que tipo de triângulo será formado:
# - equilátero: todos os lados iquais
# - isóseles: dois lados iquais                   # aqui mostrei um pouco da logica
# - escaleno: todos os lado diferentes

l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))

# podemos coloca um if dentro de outro 
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: # se pode forma um triângulo
    print('Os lados podem forma um triângulo')
    if l1 == l2 and l2 == l3:  # se 1 e iqual a 2 e 2 e iqual a 3 então 3 e automaticamente iqual a 1
        print('Triângulo equilátero')
    elif l1 == l2 and l2 != l3 or l2 == l3 and l1 != l3 or l1 == l3 and l2 != l1: # coloquei em todos apos o and l1, l2, l3 com opção de se diferente
        print('Triângulo isóseles')
    elif l1 != l2 != l3 != l1: # aqui todos tem que se diferente (DIFERENTE DO BLOCO A: tenho que compara o l3 com l1)
        print('Triângulo escaleno')
else: # ou então não pode
    print('Os lados nao podem forma um triângulo')