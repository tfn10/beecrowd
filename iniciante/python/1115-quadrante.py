def entrada():
    coordenadas = list(map(int, input().split(' ')))
    n1 = coordenadas[0]
    n2 = coordenadas[1]
    return n1, n2


def quadrante():
    while True:
        x, y = entrada()
        if x == 0 or y == 0:
            break
        elif x > 0 and y > 0:
            print('primeiro')
        elif x < 0 < y:
            print('segundo')
        elif x < 0 and y < 0:
            print('terceiro')
        elif y < 0 < x:
            print('quarto')


quadrante()
