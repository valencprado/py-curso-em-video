# programa que leia um ângulo e mostre o valor do seno, cosseno e tangente.
import math

angulo = float(input('Digite o valor de um ângulo: '))
print('O cosseno de {} é {:.2f}, o seno é {:.2f} e a tangente {:.2f}'.format(angulo, math.cos(angulo), math.sin(angulo),
                                                                             math.tan(angulo)))

# não está dando certo... (antes da correção)