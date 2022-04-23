# programa que leia o nome completo de uma pessoa
# mostrar: nome com letras maiúsculas
# com letras minúsculas
# quantas letras s/ espaço
# quantas letras o primeiro nome
nome = input("Digite seu nome completo:").strip()
nome_separado = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ","")))
print(len(nome_separado[0]))

# deu certo 🥳 código antes da aula do exercício

# correção do guanabara
# nome = str(input("Digite seu nome completo:")).strip()
#print("Analisando seu nome...")
# print("Seu nome em maiúsculas: {}".format(nome.upper()))
# print("Seu nome em minúsculas".format(nome.lower()))
# nome_separado = nome.split()
# print("Seu nome tem {} letras.".format(len(nome)-nome.count(" "))
# print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))