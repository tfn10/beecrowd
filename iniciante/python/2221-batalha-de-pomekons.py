def batalha_de_pomekons():
    numero_de_testes = int(input())
    for i in range(numero_de_testes):
        valor_do_bonus = int(input())

        valores_dabriel = list(map(int, input().split()))
        ataque_dabriel = valores_dabriel[0]
        defesa_dabriel = valores_dabriel[1]
        level_dabriel = valores_dabriel[2]

        valores_guarte = list(map(int, input().split()))
        ataque_guarte = valores_guarte[0]
        defesa_guarte = valores_guarte[1]
        level_guarte = valores_guarte[2]

        valor_bonus_dabriel = 0
        valor_bonus_guarte = 0

        if level_dabriel % 2 == 0:
            valor_bonus_dabriel = valor_do_bonus
        if level_guarte % 2 == 0:
            valor_bonus_guarte = valor_do_bonus

        valor_golpe_dabriel = (ataque_dabriel + defesa_dabriel)/2 + valor_bonus_dabriel
        valor_golpe_guarte = (ataque_guarte + defesa_guarte)/2 + valor_bonus_guarte

        if valor_golpe_dabriel > valor_golpe_guarte:
            print('Dabriel')
        elif valor_golpe_dabriel < valor_golpe_guarte:
            print('Guarte')
        else:
            print('Empate')


batalha_de_pomekons()
