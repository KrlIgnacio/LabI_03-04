# calculadora
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
print('Digite 1 para somar \nDigite 2 para subtrair \nDigite 3 para multiplicar \nDigite 4 para dividir \nDigite 5 para a potência \nDigite 6 para a radiciação')
calc = int(input())

if calc ==  1:
    res = valor1 + valor2
    print(valor1, '+', valor2, '=', '%.2f' %res)
elif calc == 2:
    res = valor1 - valor2
    print(valor1, '-', valor2, '=', '%.2f' %res)
    
elif calc == 3:
    res = valor1 * valor2
    print(valor1, 'X', valor2, '=', '%.2f' %res)
    
elif calc == 4:
    if valor2 == 0:
        print('Para efetuar a divisão, digite um valor diferente de ',valor2)
    else:
        res = valor1 / valor2
        print(valor1, ':', valor2, '=', '%.2f' %res)

elif calc == 5:
    res = valor1 ** valor2
    print(valor1, '^', valor2, '=', '%.2f' %res)
    
elif calc == 6:
    res = valor1 ** (1/valor2)
    print(valor1, '√', valor2, '=', '%.2f' %res)
    
else:
    print('Digite uma opção válida, entre 1 e 6.')