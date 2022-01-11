# programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar

# OBS: US$1.00 = R$3,27

print('==CONVERSOR==')
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 3.27
euro = real / 6.44
print('Valor em reais: {} \n Valor em dólares: {}\n Valor em euros:{}'.format(real, dolar, euro))

# deu certo 🥳 código antes de assistir à aula

# correção do guanabara
# real = float(input('Quanto dinheiro você tem na carteira? R$'))
# dolar = real / 3.27
# print('Com R${:.2f}, você pode comprar U${:.2f}'.format(real, dolar))