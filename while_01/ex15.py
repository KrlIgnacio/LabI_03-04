# imprima numero primos entre 0 e 200
# imprima a soma dos primos

i = 2  # zero e um não são primos
somaPrimos = 0

while i <= 200:
    numPrimo = True
    contPri = 2

    while contPri < i:
        if i % contPri == 0:
            numPrimo = False
            break
        contPri += 1
    
    if numPrimo: 
        print(f'{i} é primo!')
        somaPrimos += i  
    
    i += 1

print('\nSoma dos Primos: ', somaPrimos)
