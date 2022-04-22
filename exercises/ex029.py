# lê a velocidade de um carro
# se for maior que 80km/h -> multado
# multa custa 7 reais por cada km ultrapassado

vel = int(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('Pra que tanta velocidade? >:(')
    multa = (vel - 80) * 7
    print('Você pagará multa de R${},00'.format(multa))
else:
    print('Tudo tranquilo! Nada de multa')

# deu certo 🥳 (código antes da correção)