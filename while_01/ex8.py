quant = int(input('Quantos números (inteiros) você irá digitar?'))

i = 0

while i < quant:
    numeros = int(input(f'Digite o {i+1}° valor: '))
    i+=1
    
    if numeros > 0:
        print(f'{numeros} é positivo!')
    elif numeros < 0:
        print(f'{numeros} é negativo!') 
    else:
        print(f'{numeros} é zero(número neutro)!') 