# DESAFIO 63:
# Escreva um programa que mostre a sequência de Fibonacci até o n-ésimo termo.

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0  # primeiro termo
t2 = 1  # segundo termo
print(f'{t1} → {t2}', end='')  # mostra os dois primeiros

contador = 3  # começa no terceiro termo
while contador <= n:  # repete até chegar no n
    t3 = t1 + t2  # próximo termo é a soma dos dois anteriores
    print(f' → {t3}', end='')
    t1 = t2  # atualiza valores
    t2 = t3
    contador += 1

print(' → Fim')  # finaliza
