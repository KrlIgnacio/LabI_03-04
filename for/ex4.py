# vogais no texto
vogais = 'aeiou'
count_vogal = 0

texto = input('Digite um texto: ')

for letra in texto:
    if letra.lower() in vogais:
        count_vogal += 1
        
        
print(f'Seu texto tem {count_vogal} vogais! ')