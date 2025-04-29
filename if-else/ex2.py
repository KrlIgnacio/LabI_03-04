# qual numero é maior?

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um segundo valor: '))

if num1 > num2:
    print(num1, 'é maior que', num2)
    
elif num2 > num1:
    print(num2, 'é maior que', num1)

else:
    print('Os valores são iguais!')