num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
        while num1 >= num2:
            print(num1)
            num1 -= 1
else: 
    while num1 <= num2:
        print(num1)
        num1+=1