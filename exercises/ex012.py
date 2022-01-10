# algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
# preço original -5%

preco = float(input('Digite o preço: '))
desconto = (preco * 5) / 100
preco_novo = preco - desconto
print('Preço anterior: {}'.format(preco))
print('Desconto: {}'.format(desconto))
print('Preço com desconto: {}'.format(preco_novo))

# deu certo 🥳 feito antes da aula do professor
