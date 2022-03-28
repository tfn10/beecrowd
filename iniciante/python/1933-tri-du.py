def tri_du():
    """
    cartas_disponiveis = list()
    for i in range(1, 14):
        n = 0
        while n < 3:
            cartas_disponiveis.append(i)
            n += 1
    """
    cartas_recebidas = list(map(int, input().split()))
    carta1 = cartas_recebidas[0]
    carta2 = cartas_recebidas[1]
    if carta1 == carta2:
        print(carta1)
    elif carta1 > carta2:
        print(carta1)
    elif carta2 > carta1:
        print(carta2)


tri_du()
