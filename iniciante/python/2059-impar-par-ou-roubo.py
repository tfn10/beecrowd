def impar_par_ou_roubo():
    entrada = list(map(int, input().split()))

    # p representa a escolha do jogador 1
    # se p = 1 então o jogador 1 escolheu par
    # se p = 0 então o jogador 1 escolheu ímpar
    p = entrada[0]

    # j1 representa o número escolhido pelo jogador 1
    # j2 representa o número escolhido pelo jogador 2
    j1 = entrada[1]
    j2 = entrada[2]
    soma = j1 + j2

    #  r representa se o jogador 1 roubou
    # se r = 1 então o jogador 1 roubou
    # se r = 0 então o jogador 1 não roubou
    r = entrada[3]

    # a representa se o jogador 2 acusou o roubo
    # se a = 1 então o jogador 2 acusou o jogador 1 de roubo
    # se a = 0 então ele não acusou o jogador 1 de roubo
    a = entrada[4]

    if r == 1:
        if a == 0:
            print('Jogador 1 ganha!')
        elif a == 1:
            print('Jogador 2 ganha!')
    elif r == 0:
        if a == 0:
            if soma % 2 == 0:
                if p == 1:
                    print('Jogador 1 ganha!')
                elif p == 0:
                    print('Jogador 2 ganha!')
            else:
                if p == 1:
                    print('Jogador 2 ganha!')
                elif p == 0:
                    print('Jogador 1 ganha!')
        elif a == 1:
            print('Jogador 1 ganha!')


impar_par_ou_roubo()
