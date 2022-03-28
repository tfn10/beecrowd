def batmain():
    numero_de_teste = int(input())
    for i in range(numero_de_teste):
        nome_do_vilao = input()
        if nome_do_vilao.lower() == 'batmain':
            print('N')
        else:
            print('Y')


batmain()
