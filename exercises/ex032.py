# lê um ano qualquer
# verifica se é ano bissexto
ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('O ano é bissexto!')
else:
    print('Ops, esse ano não é bissexto.')


# mesmo erro do exercício 29