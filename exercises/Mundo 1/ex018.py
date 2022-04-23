# programa que leia um ângulo e mostre o valor do seno, cosseno e tangente.
import math

angulo = float(input('Digite o valor de um ângulo: '))
print('O cosseno de {} é {:.2f}, o seno é {:.2f} e a tangente {:.2f}'.format(angulo,
                                                                             math.cos(math.radians(angulo)), math.sin(math.radians(angulo)),
                                                                             math.tan(math.radians(angulo))))

# não está dando certo... (antes da correção)
# deu certo no meio da correção, ao entender o math.radius() e onde ele deve ficar.

# correção do guanabara
# from math import sin, cos, tan, radians
# angulo = float('Digite o ângulo que você deseja: ')
# seno = sin(radians(angulo))
# cosseno = cos(radians(angulo))
# tangente = tan(radians(angulo))
# print('O ângulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e
# tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))