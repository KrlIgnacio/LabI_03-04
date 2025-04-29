# letra vogal ou consoante

vogais = ['a', 'e', 'i', 'o', 'u']
vogao = ['A', 'E', 'I', 'O', 'U']

letra = input('Digite uma letra do alfabeto: ')

if letra in vogais or letra in vogao:
    print(letra, 'é uma vogal!')

else:
    print(letra, 'é uma consoante!')