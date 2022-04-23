# progrma que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias que ele foi alugado
# calcular o preço a pagar, sabendo que
# R$60,00 por dia e R$0,15 por km rodado
km = float(input('Quantos quilômetros foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
total = km * 0.15 + dias * 60
print('Com {}km percorridos e {} dias, o preço total a ser pago é de R${}.'.format(km, dias, total))

# deu certo 🥳 (tentativa antes de ver a correção)

# correção do guanabara
# dias = int(input('Quantos dias alugados?'))
# km = float(input('Quantos km rodados? '))
# pago = (dias * 60) . (km * 0.15)
# print('O total a pagar é de R${}'.format(pago))
