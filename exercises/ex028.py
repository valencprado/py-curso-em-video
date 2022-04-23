# computador "pensa" num número entre 0 e 5
# o usuário precisa descobrir o número escolhido
# se perdeu ou venceu
from random import randint
numero = randint(0, 5)
tentativa = int(input('Digite um número inteiro entre 0 e 5: '))
if tentativa == numero:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez! Tente novamente.')
    print('Número certo: {}'.format(numero))

# deu certo 🥳 (código antes da correção)

# correção do guanabara
# from random import randint
# from time import sleep
# computador = randint(0, 5)
# print('-=-'*20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-'*20)
# jogador = int(input('Em que número eu pensei? '))
# print('PROCESSANDO...')
# sleep(3)
# if jogador == computador:
#   print('PARABÉNS! Você conseguiu me vencer!')
# else:
#   print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))


