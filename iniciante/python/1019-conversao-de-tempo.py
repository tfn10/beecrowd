def conversao_tempo(tempo_em_segundo):
    restante = tempo_em_segundo
    horas = tempo_em_segundo // 3600
    restante -= horas * 3600
    minutos = restante // 60
    restante -= minutos * 60
    segundos = restante
    return print(f'{horas}:{minutos}:{segundos}')


tempo = int(input())
conversao_tempo(tempo)
