def valorPrimo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False
    return True

valor = int(input('Digite um valor inteiro: '))

if valorPrimo(valor):
    print(f'{valor} é um número primo ')
else: 
    print(f"{valor} não é primo")
    