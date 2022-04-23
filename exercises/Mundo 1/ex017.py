# progrma que leia os catetos oposto e adjacente e calcule a hipotenusa.
# usando math
import math
print('='*12)
cat_oposto = int(input('Digite o cateto oposto: '))
cat_adjacente = int(input('Digite o cateto adjacente: '))
print('Se cateto oposto vale {} e cateto adjacente vale {}, a hipotenusa vale {}'
      .format(cat_oposto, cat_adjacente, math.hypot(cat_oposto, cat_adjacente)))

print('='*12)

# deu certo 🥳 (resolução antes da correção)

# solução do guanabara

# 1 - pelo conceito matemático

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# h1 = (co ** 2 + ca ** 2) **1/2
# print(A hipotenusa vai medir {:.2f}'.format(h1))

# 2- usando math

# import hypo from math
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# h1 = math.hypo(co, ca)
# print('A hipotenusa vai medir {:.2f}'.format(h1))
