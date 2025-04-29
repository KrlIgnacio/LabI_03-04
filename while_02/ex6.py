
i = 2
soma = 0

while i > 0 and i % 2 == 0:
    i = int(input('Digite um número: '))
    if i > 0 and i % 2 == 0:
        soma += i


print('Acabou')
print(f'Soma dos valores: {soma}')