metro = float(input('Digite o metro: '))
largura = float(input('Digite a largura: '))
area = metro * largura
tinta = area / 2
print('Sua parede tem a dimensão {}x{} e a area de {}m2.'.format(metro, largura, area))
print('Para pintar sua parede precisara: {}l'.format(tinta))