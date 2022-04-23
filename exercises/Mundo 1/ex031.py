# pergunta a distância da viagem (km)
# calcula o preço da passagem de ônibus
# 0,50 por km em viagens de até 200km
# 0,45 por km em maiores viagens

viagem = float(input('Qual será a distância da viagem (em km)? '))

if viagem < 200:
    passagem = viagem * 0.5
else:
    passagem = viagem * 0.45

print('Você deverá pagar R${:.2f} de passagem.'.format(passagem))

# deu certo 🥳 (código antes da correção)

# correção do guanabara
# distância = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {}km. ')
# if distância <= 200:
#   preço = distância * 0.50
# else:
#   preço = distância * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# forma simplificada
# distância = float(input('Qual é a distância da sua viagem? '))
# preço = distância * 0.50 if distância <= 200 else distância * 0.45
# print('Você está prestes a começar uma viagem de {}km. ')
