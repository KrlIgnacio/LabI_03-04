user = 'USER10'
password = 'PASSWORD1234'
tentaivas = 0

while tentaivas <= 3:
    usuario = input('Digite o usuário:')
    senha = input('Digite o senha:')
    
    
    if usuario.upper() == user.upper() and senha.upper() == password.upper():
        print('LOGIN EFETUADO COM SUCESSO')
        break
        
    else: 
        tentaivas +=1
if tentaivas > 3:
    print('NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!')
    print('tentativas:', tentaivas)
    