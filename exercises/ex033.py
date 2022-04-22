# lê 3 números
# qual o maior e qual é o menor

n1 = float(input('Digite um número'))
n2 = float(input('Digite mais um número:'))
n3 = float(input('Mais um: '))
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))

# feito junto com o guanabara