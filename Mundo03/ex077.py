# Exercício 77 - Vogais nas palavras
# Crie uma tupla com várias palavras e mostre as vogais de cada uma.

palavras = ('aprender', 'python', 'curso', 'gratis', 'programar', 'futuro')

for termo in palavras:
    vogais = [letra for letra in termo if letra.lower() in 'aeiou']
    print(f'Na palavra {termo.upper()} temos: {" ".join(vogais)}')


