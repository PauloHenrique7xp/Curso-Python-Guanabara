# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela está o time da Chapecoense.

jogadores_famosos = ('Pelé', 'Maradona', 'Zico', 'Romário', 'Ronaldo Fenômeno', 'Ronaldinho Gaúcho', 'Neymar', 'Cristiano Ronaldo', 'Lionel Messi', 'Kylian Mbappé', 'David Beckham', 'Paolo Maldini', 'Andrés Iniesta', 'Xavi Hernández', 'Thierry Henry', 'Roberto Carlos', 'Franz Beckenbauer', 'George Best', 'Luis Suárez', 'Mohamed Salah')

print(f'Os 5 primeiro colocados são {jogadores_famosos[0:6]}')
print(f'Os 4 ultimo colocados são {jogadores_famosos[-4:]}')
print(f'Em ordem alfabética {sorted(jogadores_famosos)}')