# lê o comprimento de três retas
# se pode formar um triângulo

a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if b + c > a and a + c > b and a + b > c:
    print('É possível formar um triângulo com essas medidas!')
else: 
    print('Tá achando que é festa? Isso não forma um triângulo não >:(')


# deu certo 🥳 (código antes da correção)