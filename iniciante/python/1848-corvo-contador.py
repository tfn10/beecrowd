def corvo_contador():
    contador = 0
    soma = 0
    while contador < 3:
        grito_ou_piscada = input()
        if grito_ou_piscada == 'caw caw':
            print(soma)
            soma = 0
            contador += 1
        else:
            olho1 = grito_ou_piscada[0]
            olho2 = grito_ou_piscada[1]
            olho3 = grito_ou_piscada[2]
            if olho1 == '*':
                soma += 4
            if olho2 == '*':
                soma += 2
            if olho3 == '*':
                soma += 1


corvo_contador()
