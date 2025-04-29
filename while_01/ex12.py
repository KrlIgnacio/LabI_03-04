# colete numeros positivos e quando um numero negativo for digitado dê a média dos valores
num = 0
soma = 0
media = 0
contador = 0

print('Digite um número negativo para sair do loop!')
while num >= 0:
    num = int(input('Digite numeros positivos: '))
    soma += num 
    contador +=1

    if num < 0:
        print('número negativo digitado.')
    else:
        media =  soma / contador
print('Média dos numeros positivos: ', media)