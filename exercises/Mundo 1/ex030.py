# leia um número inteiro
# verificar se é par ou ímpar
número = int(input('Digite um número: '))
par = número % 2
if par == 0:
    print('{} é um número par!'.format(número))
else:
    print('{} é um número ímpar!'.format(número))


# não estava certo!
# número = int(input('Me diga um número qualquer: '))
# resultado = número % 2
# if resultado == 0:
#   print('O número {} é PAR'.format(número))
# else:
#   print('O número {} é ÍMPAR'.format(número))
