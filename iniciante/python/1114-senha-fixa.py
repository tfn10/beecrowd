def senha_fixa():
    while True:
        senha = int(input())
        if senha == 2002:
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')


senha_fixa()
