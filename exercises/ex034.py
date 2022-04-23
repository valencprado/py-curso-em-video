# aumento de salário de funcionários
# salário superior a 1.250 -> aumento de 10%
# inferior ou igual -> aumento de 15%

salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario_novo = salario + (salario * 10 / 100)
else:
    salario_novo = salario  + (salario * 15 / 100)

print('Parabéns! Seu novo salário é de R${:.2f}'.format(salario_novo))

# deu certo 🥳 (código antes da correção)

# correção do guanabara
# salário = float(input('Qual é o salário do funcionário? R$'))
# if salário <= 1250:
#   novo = salário + (salário * 15 / 100)
# else:
#   novo = salário + (salário * 15 / 100)
# print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))