# programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la
# cada litro de tinta pinta 2 metros quadrados

largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura * altura
tinta = area / 2

print('A área: {}'.format(area))
print('Serão necessários {} litros de tinta'.format(tinta))

# deu certo 🥳 código antes da aula do exercício

# correção do guanabara

# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} é de {}m .'.format(lar, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

