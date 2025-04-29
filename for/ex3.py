# tabuada de um numero
# numero x i
tab = 0

numero = int(input('Digite um número inteiro: '))

for i in range(0, 11):
    tab = numero * i
    print(f'{numero} X {i} = {tab}')