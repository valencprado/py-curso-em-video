# um professor quer sortear um dos quatro alunos para apagar o quadro
# programa que leia o nome dos alunos e escreva o nome do escolhido.
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')


print('Parabéns! O aluno sorteado é {}'.format((random.choice([a1, a2, a3, a4]))))

# deu certo 🥳 (feito antes da aula com ajuda da documentação da biblioteca)

# correção do guanabara

# from random import choice
# n1 = input('Primeiro aluno ')
# n2 = input('Segundo aluno ')
# n3 = input('Terceiro aluno ')
# n4 = input('Quarto aluno')
# lista = [n1, n2, n3, n4]
# escolhido = choice(lista)
# print('O aluno escolhido foi {}.'.format(escolhido))