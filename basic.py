# AULA 09
# MANIPULANDO UMA CADEIA DE CARACTERES

frase = 'Vai Corinthians'
# fatiando a frase pelo índice
print(frase[4])

# o último não entra na contagem!
print(frase[4:15])

# saltando de dois em dois:
print(frase[4:15:2])

# vai parar no 7 e começar do 0:
print(frase[:7])

# começa do 7 até o fim
print(frase[7:])

# começa do 0 e pula de 3 em 3
print(frase[0::3])

# analisando a frase

# comprimento da string
print(len(frase))

# contando elemento da string
print(frase.count('a'))

# mostra o index de algo na string
print(frase.find('Cor'))

# transformando string

# substituir algo por outra coisa
print(frase.replace('Corinthians', 'Brasil!'))

# deixando em maiúsculo ou minúsculo
print(frase.lower())
print(frase.upper())

# deixando o início da string em maiúsculo e o resto em minúsculo
print(frase.capitalize())

# deixando o início das palavras em maiúsculo
print(frase.title())

# tira espaços inúteis do início e do fim
print(frase.strip())

# r: começa pela direita e l: pela esquerda
print(frase.rstrip())
print(frase.lstrip())

# dividindo string
print(frase.split())

# juntando string
print('.'.join(frase))
