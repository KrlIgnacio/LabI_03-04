print('Please, digite 10 valores inteiros!')

contador = 0
soma = 0
while contador < 10:
    numInt = int(input(f'Digite o {contador + 1}° valor:'))
    contador+=1
    soma += numInt
    
print(f'A soma dos valores digitados é igual a {soma}!')