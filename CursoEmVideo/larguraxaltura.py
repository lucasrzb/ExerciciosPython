altura1 = float(input('Digite a altura: '))
largura2 = float(input('Digite a largura: '))
x = altura1 * largura2
litros = x / 2

print('A parede tem a dimensão {}x{} e a sua area {}m2 '.format(altura1,  largura2, x))
print('Ira gastar ao todo {}l '.format(litros))