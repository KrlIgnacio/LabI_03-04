def contaString (texto):
    # função replace() substitui uma string por outra
    caracteres_sem_espaco = texto.replace(" ", "")
    # função len() para contar as strings
    return len(caracteres_sem_espaco)

texto = input('Digite/Escreva algo aleatório: ')

resultado = contaString(texto)
print(resultado)

# GABARITO DO PROF
def quantLetras(txt):
    tam = len(txt)
    espacos = txt.count(" ")
    return tam - espacos

# txt = input('Digite um texto: ')

# x = quantLetras(txt)
# print(x)