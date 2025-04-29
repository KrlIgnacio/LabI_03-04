# numero primo

num = int(input('Digite um num:'))

i= 2

while i < num:
    if num % i == 0:
        print('Não é primo! ')
        break
    i += 1
    
else:
    print('é primo.')       
    
