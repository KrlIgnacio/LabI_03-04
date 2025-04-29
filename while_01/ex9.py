
val1 = int(input('Digite um valor inteiro: '))
val2 = int(input('Digite um segundo valor inteiro: '))


if val1 < 0 or val2 < 0:
    print('Digite um valor não negativo!')
else:
    if val1 < val2:
        maiorValor = val2
        menorValor = val1
    else:
        maiorValor = val1
        menorValor = val2
    print('Os números pares entre', menorValor, 'e', maiorValor, 'são:')
    while menorValor <= maiorValor:
            if menorValor % 2 == 0:
                print(menorValor)    
            menorValor +=1
        
    