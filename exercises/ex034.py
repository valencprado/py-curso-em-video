# aumento de salário de funcionários
# salário superior a 1.250 -> aumento de 10%
# inferior ou igual -> aumento de 15%

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 10 / 100
    salario_novo = salario + aumento
    print('Parabéns! Seu novo salário é de R${:.2f}'.format(salario_novo))
else:
    aumento = salario * 15 / 100
    salario_novo = salario  + aumento 
    print('Parabéns! Seu novo salário é de R${:.2f}'.format(salario_novo))

# deu certo 🥳 (código antes da correção)