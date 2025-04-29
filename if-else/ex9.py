# calculo nota final
# Grau A 0.3 e Grau B 0.7

gA = float(input('Digite a sua nota do Grau A:'))
gB = float(input('Digite a sua nota do Grau B:'))


if gA < 0 or gB < 0:
    print('Erro, digite notas válidas!')
    
elif gA >= 0 or gB >= 0:
        notaFinal = (gA * 0.3) + (gB * 0.7)
        if notaFinal < 6:
         print('Será necessário a realização do Grau C!')

        else:
            print('Sua nota é','%.2f' %notaFinal, '\nNão será necessário fazer o Grau C!')


    