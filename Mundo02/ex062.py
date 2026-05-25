# DESAFIO 62:
# Melhore o DESAFIO 61, perguntando ao usuário se ele quer mostrar mais termos.
# O programa encerra quando o usuário disser que não quer mais.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro  # começa no primeiro termo
contador = 1      # controla quantos termos já foram mostrados
total = 0         # total de termos mostrados
mais = 10         # começa mostrando 10 termos

while mais != 0:  # repete enquanto o usuário pedir mais termos
    total += mais  # soma ao total
    while contador <= total:  # mostra até o total pedido
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))  # pergunta novos termos

print(f'Progressão finalizada com {total} termos mostrados.')

