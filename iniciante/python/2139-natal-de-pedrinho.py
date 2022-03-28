def natal_de_pedrinho():
    while True:
        try:
            dias_de_cada_mes = {
                1: 31,
                2: 29,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
            }
            mes_e_dia = list(map(int, input().split()))
            mes = mes_e_dia[0]
            dia = mes_e_dia[1]
            total_de_dias = 0
            natal = 0
            for i in range(1, 12):
                natal += dias_de_cada_mes[i]
            natal += 25
            if mes == 12 and dia == 24:
                print('E vespera de natal!')
            elif mes == 12 and dia > 25:
                print('Ja passou!')
            elif mes == 12 and dia == 25:
                print('E natal!')
            else:
                for m in range(1, mes):
                    total_de_dias += dias_de_cada_mes[m]
                total_de_dias += dia
                dias_faltam_natal = natal - total_de_dias
                print(f'Faltam {dias_faltam_natal} dias para o natal!')
        except ValueError:
            break
        except EOFError:
            break
        except IndexError:
            break


natal_de_pedrinho()
