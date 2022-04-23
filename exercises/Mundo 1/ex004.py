#  programa que leia algo do teclado e mostre o seu tipo primitivo e várias informações sobre ele
algo = input('Digite algo: ')

print('O tipo dele é:', type(algo))

print('Ele é alfanumérico?', algo.isalnum())
print('Ele está em letras maiúsuclas?', algo.isupper())
print('Ele está em letras minúsculas?', algo.islower())
print('Ele é numérico?', algo.isnumeric())
print('Ele só possui letras?', algo.isalpha())
print('É só espaço?', algo.isspace())
print('Está capitalizada?', algo.istitle())

#  métodos -> funcionalidades do objeto(variável)
