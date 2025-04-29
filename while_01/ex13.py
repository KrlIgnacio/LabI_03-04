# fatorial

i = 1
fatorial = 1

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print('Número negativo, favor digitar um valor positivo.')
else:
    while i <= numero:
        fatorial = fatorial * i
        i+= 1
    
    print(f"O fatorial de {numero} é {fatorial}")

