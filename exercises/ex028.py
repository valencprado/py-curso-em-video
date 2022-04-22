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