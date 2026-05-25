# DESAFIO 61:
# Refaça o DESAFIO 51, mostrando os 10 primeiros termos de uma PA
# usando a estrutura while.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro  # começa no primeiro termo
contador = 1      # controla quantos termos já foram mostrados

while contador <= 10:  # repete até mostrar 10 termos
    print(termo, end=' → ')  # mostra o termo atual
    termo += razao           # soma a razão para o próximo termo
    contador += 1            # aumenta o contador

print('Fim')  # finaliza
