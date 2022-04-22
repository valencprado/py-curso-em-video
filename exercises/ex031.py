# pergunta a distância da viagem (km)
# calcula o preço da passagem de ônibus
# 0,50 por km em viagens de até 200km
# 0,45 por km em maiores viagens

viagem = int(input('Qual será a distância da viagem (em km)? '))

if viagem < 200:
    passagem = viagem * 0.5
    print('Você deverá pagar R${} de passagem'.format(passagem))
else:
    passagem = viagem * 0.45
    print('Você deverá pagar R${} de passagem.'.format(passagem))

# deu certo 🥳 (código antes da correção)