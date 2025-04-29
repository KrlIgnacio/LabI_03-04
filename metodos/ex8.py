def contador(x):
    if x > 0:
        print(f"Contando de 1 até {x}:")
        for i in range(1, x+1):
            print(i)
    else:
        print('Digite um valor positivo: ') 
           
x = int(input('Digite um valor inteiro: '))

contador(x)