def diferenca(a, b, c, d):
    dif = a * b - c * d
    return print(f'DIFERENCA = {dif}')


def entrada():
    valor = int(input())
    return valor


n1 = entrada()
n2 = entrada()
n3 = entrada()
n4 = entrada()
diferenca(n1, n2, n3, n4)
