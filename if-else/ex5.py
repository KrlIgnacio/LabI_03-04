# faixa de preço - produtos

preco = float(input('Digite o valor de um produto R$: '))

if preco <= 0:
    print('Preço inválido!')

elif preco > 0 and preco <= 30:
    print('Preço baixo!')

elif preco > 30 and preco <= 50:
    print('Preço médio!')
    
else:
    print('Preço ALTO!')