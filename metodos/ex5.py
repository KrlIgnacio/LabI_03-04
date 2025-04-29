def exibirLista(lista):
    for itens in lista:
        print(itens.strip())

lista = str(input('Digite a sua lista: '))
res = lista.split(',')

exibirLista(res)
