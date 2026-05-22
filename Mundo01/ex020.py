# DESAFIO:
# O mesmo professor quer sortear a ordem de apresentação dos trabalhos dos alunos.

from random import shuffle # fução de embaralha a lista

alunos = ['Paulo', 'Maria', 'Eduardo', 'Ana']

# embaralhando
shuffle(alunos)

print(f'A ordem de aprensetação será:')
print(alunos)