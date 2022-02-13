# agora será sorteado a ordem de apresentação dos quatro alunos
# programa que leia o nome dos alunos e mostre a ordem.

from random import shuffle
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Por fim, digite o nome de mais um aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Ordem das apresentações: {}'.format(lista))

# não está dando certo... (antes da correção)

# correção do guanabara
# from random import shuffle
# n1 = input('Primeiro aluno: ')
# n2 = input('Segundo aluno: ')
# n3 = input('Terceiro aluno: ')
# lista = [n1, n2, n3, n4]
# shuffle(lista)
# print('A ordem de apresentação será: ')
# print(lista)