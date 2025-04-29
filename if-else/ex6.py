# aplicando juros a preços

valorP = float(input('Digite o valor de um produto R$: '))

if valorP < 100:
    novoValor = (valorP * 0.1) + valorP
    print('Valor após os juros: R$', novoValor)
    
elif valorP >= 100 and valorP < 300:
    novoValor = (valorP * 0.2) + valorP
    print('Valor após os juros: R$', novoValor)

elif valorP >= 300 and valorP < 1000:
    novoValor = (valorP * 0.5) + valorP
    print('Valor após os juros: R$', novoValor)
    
elif valorP < 0:
    print('Digite um valor positivo.')
else:
    print('Valor muito alto, nenhuma taxa aplicada.')