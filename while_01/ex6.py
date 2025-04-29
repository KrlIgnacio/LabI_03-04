
print('Vamos brincar! Você digita 20 numeros float(decimais) e eu os armazeno.')
cont = 0
concatStr = ''
while cont < 20:
    numeros = str(input(f'Digite o {cont + 1}° valor: '))
    cont +=1
    concatStr += numeros + ' '

print('Você digitou:',concatStr.strip())