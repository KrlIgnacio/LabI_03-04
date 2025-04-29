def menor_palavra(lista):
    if lista:
        return min(lista, key=len)
    else:
        return "A Lista está vazia!"
    
lista = input('Digite palavras separadas por vírgula: ').split(',')
menor = menor_palavra(lista)

print(f'A menor palavra é: {menor}')