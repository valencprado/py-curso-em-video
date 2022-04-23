# lê um ano qualquer
# verifica se é ano bissexto
ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('Ops, esse ano não é bissexto.')


# mesmo erro do exercício 30 - corrigido antes da correção

# correção do guanabara
# from datetime import date
# ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
# if ano == 0:
#   ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#   print('O ano {} é BISSEXTO.'.format(ano))
# else:
#   print('O ano {} NÃO é BISSEXTO.'.format(ano))