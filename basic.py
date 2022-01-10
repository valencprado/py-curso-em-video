#  AULA 07



# adição -> +
# subtração -> -
# multiplicação -> *
# divisão -> /
# potenciação -> **
# divisão inteira -> //
# resto da divisão -> %

# ORDEM DE PRECEDÊNCIA -> QUAIS SÃO EXECUTADOS PRIMEIRO?

# nome = input('Qual é seu nome? ')
# print('Prazer, {:=^20}!'.format(nome))
# print('Prazer, {:^20}!'.format(nome))
# print('Prazer, {:>20}!'.format(nome))
# print('Prazer, {:>20}!'.format(nome))
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+ n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma vale {}, o produto  {} e a divisão é {:2f}'.format(s, m, d), end='. ')
print('A divisão inteira é {} e a potência {}'.format(di, e))

#

