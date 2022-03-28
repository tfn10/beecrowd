def tempo_de_evento(dia_inicial, hora_inicial, minuto_inicial, segundo_inicial,
                    dia_final, hora_final, minuto_final, segundo_final):
    segundos_totais_inicial = dia_inicial * 86400 + hora_inicial * 3600 + minuto_inicial * 60 + segundo_inicial
    segundos_totais_final = dia_final * 86400 + hora_final * 3600 + minuto_final * 60 + segundo_final
    diferenca = segundos_totais_final - segundos_totais_inicial
    dias_de_evento = diferenca // 86400
    resto = diferenca % 86400
    horas_de_evento = resto // 3600
    resto = resto % 3600
    minutos_de_evento = resto // 60
    resto = resto % 60
    segundos_de_evento = resto
    return print(f'{dias_de_evento} dia(s)\n'
                 f'{horas_de_evento} hora(s)\n'
                 f'{minutos_de_evento} minuto(s)\n'
                 f'{segundos_de_evento} segundo(s)')


def entrada_dia():
    dia = input().split(' ')
    del dia[0]
    dia = int(dia[0])
    return dia


def entrada_horario():
    horario = list(map(int, input().split(' : ')))
    horas = horario[0]
    minutos = horario[1]
    segundos = horario[2]
    return horas, minutos, segundos


dia_i = entrada_dia()
hora_i, minuto_i, segundo_i = entrada_horario()
dia_f = entrada_dia()
hora_f, minuto_f, segundo_f = entrada_horario()
tempo_de_evento(dia_i, hora_i, minuto_i, segundo_i, dia_f, hora_f, minuto_f, segundo_f)
