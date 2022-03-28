def mjolnir():
    numero_de_testes = int(input())
    for i in range(numero_de_testes):
        teste = input().split()
        pessoa = teste[0]
        forca_aplicada = int(teste[1])
        if pessoa == 'Thor':
            print('Y')
        else:
            print('N')


mjolnir()
