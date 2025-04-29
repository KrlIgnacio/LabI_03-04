def valorDivisivel(valor1, valor2):
    return valor1 % valor2 == 0

val1 = int(input('Digite o primeiro valor: '))

val2 = int(input('Digite o outro valor: '))

r = valorDivisivel(val1, val2)
print(r)