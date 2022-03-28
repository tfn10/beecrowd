def entrada():
    tempo = list(map(int, input().split()))
    hora_inicial = tempo[0]
    minuto_inicial = tempo[1]
    hora_final = tempo[2]
    minuto_final = tempo[3]
    return hora_inicial, minuto_inicial, hora_final, minuto_final


def tempo_de_jogo():
    hora_i, minuto_i, hora_f, minuto_f = entrada()
    minutos_totais_jogado = (hora_f - hora_i) * 60 + minuto_f - minuto_i
    hora_jogada = 0
    minuto_jogado = 0
    if minutos_totais_jogado > 0:
        hora_jogada = minutos_totais_jogado // 60
        minuto_jogado = minutos_totais_jogado % 60
    elif minutos_totais_jogado < 0:
        minutos_totais_jogado = 24 * 60 + minutos_totais_jogado
        hora_jogada = minutos_totais_jogado // 60
        minuto_jogado = minutos_totais_jogado % 60
    else:
        hora_jogada = 24
        minuto_jogado = 0
    print(f'O JOGO DUROU {hora_jogada} HORA(S) E {minuto_jogado} MINUTO(S)')


tempo_de_jogo()
