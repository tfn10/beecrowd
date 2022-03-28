def area_triangulo_retangulo(a, c):
    """a área do triângulo retângulo que tem A por base e C por altura."""
    area_triangulo_retan = (a * c)/2
    return print(f'TRIANGULO: {area_triangulo_retan:.3f}')


def area_circulo(c):
    """a área do círculo de raio C. (pi = 3.14159)"""
    area_circ = 3.14159 * (c ** 2)
    return print(f'CIRCULO: {area_circ:.3f}')


def area_trapezio(a, b, c):
    """a área do trapézio que tem A e B por bases e C por altura."""
    area_trape = (a + b)/2 * c
    return print(f'TRAPEZIO: {area_trape:.3f}')


def area_quadrado(b):
    """a área do quadrado que tem lado B."""
    area_quad = b ** 2
    return print(f'QUADRADO: {area_quad:.3f}')


def area_retangulo(a, b):
    """a área do retângulo que tem lados A e B."""
    area_retan = a * b
    return print(f'RETANGULO: {area_retan:.3f}')


def entrada():
    lados = input().split(' ')
    lado_a = float(lados[0])
    lado_b = float(lados[1])
    lado_c = float(lados[2])
    return lado_a, lado_b, lado_c


valor_a, valor_b, valor_c = entrada()
area_triangulo_retangulo(valor_a, valor_c)
area_circulo(valor_c)
area_trapezio(valor_a, valor_b, valor_c)
area_quadrado(valor_b)
area_retangulo(valor_a, valor_b)
