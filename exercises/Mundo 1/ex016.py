# Programa que leia um número real qualquer e mostre sua porção inteira.
import math
num = float(input('Digite um número real: '))

print('A porção inteira de {} é {}'.format(num, math.trunc(num)))

# deu certo 🥳 (antes de ver a solução)

# correção do guanabara 
# from math import trunc
# num = float(input('Digite um valor: '))
# print('O valor foi {} e a sua porção inteira é {}'.format(num, trunc(num)))


# só importar o truncate()
# usar trunc() ao invés de floor() para mostrar a parte inteira e não arredondar

# sem biblioteca:

# num = float(input('Digite um valor: ))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

# mostra a porção inteira