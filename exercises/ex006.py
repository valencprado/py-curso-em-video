# algoritmo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada.

numero = float(input('Digite um número:'))

print('Número digitado: {} \n Dobro: {} \n Triplo: {} \n raiz quadrada: {}'.format(numero, numero*2, numero*3, numero**(1/2)))

# deu certo 🥳 (versão sem ter assistido a aula)

# correção do professor

# n = int(input('Digite um número: '))
# d = n  * 2
# t = n * 3
# r = n ** (1/2)

# print('O dobro de {} vale {}'.format(n, d))
# print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {}'.format(n, t, n r)

# versão simplificada -> print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:2f}.'format(n, (n+3), n, n**(1/2) ou pow(n, 1/2))