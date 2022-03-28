def cachorros_quentes():
    entrada = list(map(int, input().split()))
    cachorros_quentes_consumidos = entrada[0]
    total_de_participantes = entrada[1]
    cachorros_quentes_consumidos_medio = float(cachorros_quentes_consumidos / total_de_participantes)
    print(f'{cachorros_quentes_consumidos_medio:.2f}')


cachorros_quentes()
