# # verificar se a cidade está dentro da tupla.
# e mostra o indice dela

cidade_brasileiras = ('Acre', 'Bahia', 'Rio de janeiro', 'São paulo', 'Salvador')

nome_de_uma_cidade = input('Informe o nome de uma cidade brasileira: ').strip().capitalize()
if nome_de_uma_cidade in cidade_brasileiras:
    print(f'A cidade {nome_de_uma_cidade} está no indice {cidade_brasileiras.index(nome_de_uma_cidade)}')
else:
    print('Cidade não foi encontrada')