# algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
# preço original -5%

preco = float(input('Digite o preço: '))

preco_novo = preco - (preco * 5) / 100
print('Preço anterior: {:.2f}'.format(preco))
print('Preço com desconto: {:.2f}'.format(preco_novo))

# deu certo 🥳 feito antes da aula do professor

# correção do guanabara
# preço = float(input('Qual o preço do produto? R$'))
# novo = preco - (preco * 5/100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))