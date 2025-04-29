def somaValor(v):
    soma = 0
    for i in range(0, v + 1):
        soma += i
    return soma
       
    
val = int(input('Digite um valor: '))

resultado = somaValor(val)
if resultado > 0:
   print(f'A soma de 0 a {val} é igual a {resultado}')
else:
   print('Valor negativo')
 
