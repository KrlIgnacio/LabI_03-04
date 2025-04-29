# armazene prod em uma lista e depois os imprima
lista_compras = []

quant = int(input('Quantos produtos você deseja adicionar a sua lista de compras: '))

for lista in range(0, quant):
    lista_compras.append(input('Digite o produto: '))

print('\nLista de Compras: ')

for i in lista_compras:
    print(i)