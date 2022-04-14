# programa que leia uma frase
# conte quantas vezes aparece a letra a
# posição da primeira vez que aparece
# posição da última vez que aparece
frase = input("Digite uma frase: ")
contagem = frase.count("a")
primeiro = frase.find("a")
ultimo = frase.rfind("a")
print("Quantas letras a:".format(contagem))
print("Posição da primeira:".format(primeiro))
print("Posição da última: ".format(ultimo))

# funcionando!