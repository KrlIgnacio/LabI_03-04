solteiras = []
casadas = []
viuvas = []
divorciadas = []

for pessoas in range(1, 20):
    nome = input(f'{pessoas}° pessoa digite seu nome: ')
    estadoCivil = input(f'{pessoas}° pessoa digite seu estado civil: ')
    if (estadoCivil == 'solteiro' or estadoCivil == 'solteira'):
        solteiras.append(nome)
    elif (estadoCivil == 'casada' or estadoCivil == 'casado'):
        casadas.append(nome)
    elif (estadoCivil == 'viuva' or estadoCivil == 'viuvo'):
         viuvas.append(nome)
    elif (estadoCivil == 'divorciada' or estadoCivil == 'divorciado'):
        divorciadas.append(nome)
    else:
        print('Estado Civil inválido!')
        
print ('Pessoas Solteiras: ')
print(solteiras)
print ('Pessoas Casadas: ')
print(casadas)
print ('Pessoas Divorciadas: ')
print(divorciadas)
print ('Pessoas Viúvas: ')
print(viuvas)