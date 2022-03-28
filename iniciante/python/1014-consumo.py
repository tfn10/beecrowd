def consumo_medio(distancia_total, combustivel_gasto):
    consumo = distancia_total / combustivel_gasto
    return print(f'{consumo:.3f} km/l')


distancia = int(input())
total_combustivel_gasto = float(input())
consumo_medio(distancia, total_combustivel_gasto)
