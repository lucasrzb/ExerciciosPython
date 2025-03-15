carteira = float(input('Digite o saldo da carteira R$: '))
#cambio = float(input('Digite a atual taxa de cambio em dolar: ')) #USE . EM VEZ ,
x = carteira / 5.8 # 5.8 cotação do dolar
y = carteira / 6.23 #6.23 cotação do euro
print('O valor de compra em Dólar US$ {:.2f}'.format(x))
print('O valor de compra em Euro EUR$ {:.2f}'.format(y))