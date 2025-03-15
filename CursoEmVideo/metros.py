metro = float(input('Digite o metro: '))
x = metro * 100 # 1mt = 100 centimetros
y = metro * 1000 # 100cen = 1000 mil
km = metro / 1000
deca = metro / 10
dec = metro * 10

print('Valor em Centimetro: {:.0f}cm'.format(x))
print('Valor em Milímetros: {:.0f}mm'.format(y))
print('Valor em Quilometro: {}km'.format(km))
print('Valor em Decametro: {:.0f}.dc'.format(deca))
print('Valor em Decimetro: {}.dm'.format(dec))