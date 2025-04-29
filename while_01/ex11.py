
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
par = 0
impar = 0

if v1 < v2:
    maiorV = v2
    menorV = v1
else:  
    maiorV = v1
    menorV = v2
    
while menorV <= maiorV:
    if menorV % 2 == 0:
        par += menorV
    else: 
        impar += menorV
    menorV += 1

print(f'Dado o intervalo {v1} e {v2}:')
print(f'A soma dos valores pares: {par}')
print(f'A soma dos valores impares: {impar}')