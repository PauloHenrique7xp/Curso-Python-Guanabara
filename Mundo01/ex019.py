# DESAFIO:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.

from random import choice  # importei so uma função do random, enconomizando memória

alunos = ['Paulo', 'Maria', 'Eduardo', 'Ana']

# escolha aleatoria
escolhido = choice(alunos)

print(f'O aluno sorteado foi {escolhido}')
