def tempo_jogo(tempo_inicial, tempo_final):
    if tempo_inicial < tempo_final:
        tempo_jogado = tempo_final - tempo_inicial
    elif tempo_inicial > tempo_final:
        tempo_jogado = 24 - tempo_inicial + tempo_final
    else:
        tempo_jogado = 24
    return print(f'O JOGO DUROU {tempo_jogado} HORA(S)')


def entrada():
    tempos = list(map(int, input().split(' ')))
    horario_inicial = tempos[0]
    horario_final = tempos[1]
    return horario_inicial, horario_final


inicial, final = entrada()
tempo_jogo(inicial, final)
