def coordenadas(eixo_x, eixo_y):
    # origem
    if eixo_x == eixo_y == 0.0:
        return print('Origem')

    # primeiro quadrante
    elif eixo_x > 0.0 and eixo_y > 0.0:
        return print('Q1')

    # segundo quadrante
    elif eixo_x < 0.0 and eixo_y > 0:
        return print('Q2')

    # terceiro quadrante
    elif eixo_x < 0.0 and eixo_y < 0.0:
        return print('Q3')

    # quarto quadrante
    elif eixo_x > 0.0 and eixo_y < 0.0:
        return print('Q4')

    # eixo x
    elif eixo_x != 0 and eixo_y == 0:
        return print('Eixo X')

    # eixo y
    elif eixo_x == 0 and eixo_y != 0:
        return print('Eixo Y')


def entrada():
    pontos = input().split(' ')
    x = float(pontos[0])
    y = float(pontos[1])
    return x, y


coordenada_x, coordenada_y = entrada()
coordenadas(coordenada_x, coordenada_y)
