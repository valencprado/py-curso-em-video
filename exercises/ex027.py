# programa que leia o nome completo de alguém
# mostrar o primeiro nome e o último separados
nome = input("Digite seu nome completo: ")
separado = nome.split()
# contrario = nome.rsplit()
nomes = len(nome.split())
print(nomes)
primeiro = separado[0]
# ultimo = separado[nomes]
print("Primeiro: {}".format(primeiro))
# print("último: {}".format(ultimo))

# erro: não conseguir achar o último nome