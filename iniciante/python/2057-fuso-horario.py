def fuso_horario():
    entrada = list(map(int, input().split()))
    hora_da_saida = entrada[0]
    tempo_de_viagem = entrada[1]
    fuso = entrada[2]
    hora_local = hora_da_saida + tempo_de_viagem + fuso
    if hora_local == 24:
        print(0)
    elif hora_local < 0:
        hora_local += 24
        print(hora_local)
    elif hora_local > 24:
        hora_local -= 24
        print(hora_local)
    else:
        print(hora_local)


fuso_horario()
