
vA = int(input('Digite um valor inteiro para A:'))
vB = int(input('Digite um valor inteiro para B:'))

if vB == 0:
    print('Defina um valor diferente de zero para B!')

else:
   divisao =  vA / vB 
   print(vA, 'dividido por', vB, 'é igual a', '%.2f' %divisao)