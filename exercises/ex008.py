# programa que leia o valor em metros e mostre convertido em centímetros e milímetros.

metro = float(input('Digite o valor em metros: '))
# colocando as outras medidas (desafio)
# km dam hm m dm cm mm
km = metro / 1000
dam = metro / 100
hm = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('Em metros: {}'.format(metro))
print('Essa medida equivale a')
print('{}km, {}dam, {}hm'.format(km, dam, hm))
print('{}dm, {}cm e {}mm'.format(dm, cm, mm))
# deu certo 🥳 (versão antes de assistir a aula do exercício

# correção do guanabara

# ao invés de converter apenas para centímetros e milímetros, outras formas são feitas

# medida = float(input('Uma distância em metros'))
# cm = medida * 100
# mm = medida * 1000
# print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))



