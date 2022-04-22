# AULA 10
# IF E ELSE
# condições 

# exemplo de condição simples
# nome = str(input('Qual seu nome? '))

# if nome == 'Valentina': 
#     print('Belo nome!')
# else:
#     print('É... seu nome é ok.')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))

if m >= 6:
    print('Parabéns!')
else:
    print('Vish... tá precisando estudar!')