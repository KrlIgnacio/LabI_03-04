
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um segundo valor: '))
num3 = int(input('Digite um terceiro valor: '))

if num1 > num2 and num1 > num3:
    print(num1,'é maior que', num2, 'e', num3)

elif num2 > num1 and num2 > num3:
    print(num2,'é maior que', num1, 'e', num3)

elif num3 > num1 and num3 > num2:
    print(num3,'é maior que', num2, 'e', num1)
else:
    print('Ambos os valores são iguais.')