# programa que leia uma frase
# conte quantas vezes aparece a letra a
# posição da primeira vez que aparece
# posição da última vez que aparece
frase = input("Digite uma frase: ").lower().strip()
contagem = frase.count("a")
primeiro = frase.find("a")
ultimo = frase.rfind("a")
print("Quantas letras a: {}".format(contagem))
print("Posição da primeira: {}".format(primeiro + 1))
print("Posição da última: {}".format(ultimo + 1))

# funcionando!

# correção do guanabara
# frase = str(input("Digite uma frase: ")).lower().strip()
# print("A letra A aparece {} vezes na frase".format(frase.count("a")))
# print("A primeira letra A aparece na {} posição".format(frase.find("a")+1))
# print("A primeira letra A aparece na {} posição".format(frase.rfind("a")+1))