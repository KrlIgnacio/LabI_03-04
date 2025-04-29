def maiorValor(v1, v2, v3):
    if (v1 > v2) and (v1 > v3):
        return v1
    elif (v2 > v1) and (v2 > v3):
        return v2
    else:
        return v3
        
val1 =  int(input('Digite um valor: '))
val2 =  int(input('Digite um segundo valor: '))
val3 =  int(input('Digite um terceiro valor: '))

resultado = maiorValor(val1, val2, val3)
print(resultado)