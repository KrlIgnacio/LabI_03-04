def notaConceito(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media > 0 and media <= 4:
       print('Média: D.') 
    elif media > 4 and media <= 7:
        print('Média: C.')
    elif media > 7 and media <= 9:
        print('Média: B.')
    elif media > 9 and media <= 10:
        print('Média: A.')
    else:
        print('Erro: Média fora do intervalo esperado')

print('Cálculo de Conceito de Nota:')

n1 = float(input('Digite a sua N1: '))
n2 = float(input('Digite a sua N2: '))
n3 = float(input('Digite a sua N3: '))

if n1 < 0 or n2 < 0 or n3 < 0:
    print("ERRO")
else:
    notaConceito(n1, n2, n3)