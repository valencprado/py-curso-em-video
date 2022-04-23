# lê a velocidade de um carro
# se for maior que 80km/h -> multado
# multa custa 7 reais por cada km ultrapassado

vel = float(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('Pra que tanta velocidade? >:(')
    multa = (vel - 80) * 7
    print('Você pagará multa de R${},00'.format(multa))
else:
    print('Tudo tranquilo! Nada de multa')

# deu certo 🥳 (código antes da correção)

# correção do guanabara 
# velocidade = float(input('Qual é a velocidade atual do carro? '))
# if velocidade > 80:
#   print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
#   multa = (velocidade - 80 )* 7
#   print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')