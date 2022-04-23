# lê o comprimento de três retas
# se pode formar um triângulo

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if b + c > a and a + c > b and a + b > c:
    print('É possível formar um triângulo com essas medidas!')
else: 
    print('Tá achando que é festa? Isso não forma um triângulo não >:(')


# deu certo 🥳 (código antes da correção)

# correção do guanabara

# print('-=-'* 20)
# print('Analisador de Triângulo')
# r1 = float(input('Primeiro segmento: ')) 
# r2 = float(input('Segundo segmento: ')) 
# r3 = float(input('Terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#   print('Os segmentos PODEM formar um triângulo!')
# else:
#   print('Os segmentos NÃO PODEM formar um triângulo!')
