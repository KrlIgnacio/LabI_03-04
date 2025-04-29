num1 = int(input('Digite um valor: '))
num2 = int(input('Digite segundo valor: '))

if num2 > num1:
    print('O primeiro valor deve ser maior que o primeiro!')

else: 
    for i in range(num1, num2+1):
        print(i)