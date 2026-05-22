# DESAFIO:
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip()

# upper deixa tudo maiúsculo pra não dar erro de comparação
print('A cidade começa com SANTO?', cidade.upper().startswith('SANTO')) # startswith verifica se a primeira palavra começa com SANTO
