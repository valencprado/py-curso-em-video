# programa que leia o nome completo de alguém
# mostrar o primeiro nome e o último separados
nome = input("Digite seu nome completo: ").strip()
separado = nome.split()
# contrario = nome.rsplit()
nomes = len(separado)
primeiro = separado[0]
print("Primeiro: {}".format(primeiro))
print("último: {}".format(separado[len(separado)-1]))

# erro: não conseguir achar o último nome

# correção do guanabara

# n = str(input("Digite seu nome completo: ")).strip()
# print("Muito prazer em te conhecer!")
# print("Seu primeiro nome é: {}".format(nome[0]))
# print("Seu último nome é: {}".format(separado[len(nome)-1]))