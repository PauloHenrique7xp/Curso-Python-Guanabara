contagem = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
  num = int(input('Informe um número de 0 ate 20 '))
  if 1 <= num <= 20:
    print(f'Número escolhido foi {contagem[num - 1]}')
    break