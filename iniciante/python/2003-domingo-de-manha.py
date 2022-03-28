def domingo_de_manha():
    while True:
        try:
            horario = input()
            horas = int(horario[:horario.index(':')])
            minutos = int(horario[horario.index(':')+1:])
            minutos_totais = horas * 60 + minutos
            horario_do_terminal = 8 * 60
            atraso_maximo = minutos_totais - horario_do_terminal + 60
            if atraso_maximo <= 0:
                print(f'Atraso maximo: 0')
            else:
                print(f'Atraso maximo: {atraso_maximo}')
        except EOFError:
            break
        except ValueError:
            break


domingo_de_manha()
