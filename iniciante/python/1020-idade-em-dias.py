def idade_em_dias(d):
    dias = {'ano(s)': 365, 'mes(es)': 30, 'dia(s)': 1}
    dias_restantes = d
    for ano_mes_dia, n_dias in dias.items():
        dia = dias_restantes // n_dias
        dias_restantes -= dia * n_dias
        print(f'{dia} {ano_mes_dia}')


total_dias = int(input())
idade_em_dias(total_dias)
