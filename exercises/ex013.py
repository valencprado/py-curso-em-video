# algoritmo que leia o salário e dê 15% de aumento
# salário antigo + 15%

salario = float(input('Digite seu salário: '))
aumento = (salario * 15) / 100
salario_novo = salario + aumento
# ou salario_novo = salario + (salario * 15 / 100)
print('Parabéns! agora seu salário é de: R${:.2f}'.format(salario_novo))

# deu certo 🥳 (feito antes da aula)

# correção do guanabara
# salário = float(input('Qual é o salário do funcionário? R$'))
# novo = salario + (salario * 15 / 100)
# print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
