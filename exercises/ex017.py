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
