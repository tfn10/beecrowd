import math


def delta(a, b, c):
    valor_delta = b ** 2 - 4 * a * c
    return valor_delta


def raizes(a, b, c):
    valor_de_delta = delta(a, b, c)
    if valor_de_delta < 0 or a == 0:
        return print('Impossivel calcular')
    else:
        r1 = (-b + math.sqrt(valor_de_delta))/(2*a)
        r2 = (-b - math.sqrt(valor_de_delta))/(2*a)
        return print(f'R1 = {r1:.5f}\n'
                     f'R2 = {r2:.5f}')


def entrada():
    valores = input().split(' ')
    valor_a = float(valores[0])
    valor_b = float(valores[1])
    valor_c = float(valores[2])
    return valor_a, valor_b, valor_c


n1, n2, n3 = entrada()
raizes(n1, n2, n3)
