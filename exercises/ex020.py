# agora será sorteado a ordem de apresentação dos quatro alunos
# programa que leia o nome dos alunos e mostre a ordem.

import random
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Por fim, digite o nome de mais um aluno: ')

print('Ordem das apresentações: {}'.format(random.shuffle([a1, a2, a3, a4])))

# não está dando certo... (antes da correção)
