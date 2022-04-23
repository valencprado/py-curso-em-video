# programa que leia um número e mostre cada dígito separado
numero = (input("Digite um número grande!"))
# print(' '.join(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 
print("Unidade: ".format(u))
print("Dezena: ".format(d))
print("Centena: ".format(c))
print("Milhar: ".format(m))


# deu certo 🥳 código antes de assistir à aula

# correção do guanabara
# num = int(input("Digite um número: "))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print("analisando o número {}...".format(num))
# print("Unidade: {}".format(u))
# print("Dezena: {}".format(d))
# print("Centena: {}".format(c))
# print("Milhar: {}".format(m))