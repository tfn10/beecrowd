def combustivel_gasto(tempo_gasto, velocidade_media):
    # automóvel faz 12 Km/L
    gasto_em_litro = tempo_gasto * velocidade_media * (1/12)
    return print(f'{gasto_em_litro:.3f}')


tempo = int(input())
velocidade = int(input())
combustivel_gasto(tempo, velocidade)
