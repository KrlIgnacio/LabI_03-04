
print('Vamos brincar de descobrir o time de futebol...\n')

qtd_torcedores = 1
imortal = 0

while qtd_torcedores <= 10:
    time = input(f' {qtd_torcedores}° usuário, digite o seu time: ')
    qtd_torcedores +=1
    if time == 'gremio' or time == 'Gremio' or time == 'grêmio' or time == 'Grêmio':
        imortal += 1
              
if imortal > 0:
    print('Torcedores do Grêmio: ', imortal) 
else:
    print('Que pena, nenhum usuário torce para o Imortal!')