user = 'USER10'
password = 'PASSWORD1234'


while True:
    usuario = input('Digite o usuário: ')
    senha = input('Digite o senha: ')
    
    if usuario.upper() == user.upper() and senha.upper() == password.upper():
        print('LOGIN EFETUADO COM SUCESSO')
        break
    else: 
        print('Usuário ou senha incorretos.')