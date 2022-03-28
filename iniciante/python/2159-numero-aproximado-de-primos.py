import math


def numero_aproximado_primo():
    n = int(input())
    valor_minimo = float(n / math.log(n))
    valor_maximo = float(1.25506*valor_minimo)
    print(f'{valor_minimo:.1f} {valor_maximo:.1f}')


numero_aproximado_primo()
