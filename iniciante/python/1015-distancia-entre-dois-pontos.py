import math


def entrada():
    a = input().split(' ')
    a1 = float(a[0])
    a2 = float(a[1])
    return a1, a2


def distancia_dois_pontos(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return print(f'{distancia:.4f}')


valor_x1, valor_y1 = entrada()
valor_x2, valor_y2 = entrada()
distancia_dois_pontos(valor_x1, valor_y1, valor_x2, valor_y2)
