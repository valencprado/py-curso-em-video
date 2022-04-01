# programa que leia o nome completo de uma pessoa
# mostrar: nome com letras maiúsculas
# com letras minúsculas
# quantas letras s/ espaço
# quantas letras o primeiro nome
nome = input("Digite seu nome completo:")
nome_separado = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ","")))
print(len(nome_separado[0]))

# deu certo 🥳 código antes da aula do exercício