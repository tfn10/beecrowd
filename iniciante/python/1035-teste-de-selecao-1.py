def selecao(a, b, c, d):
    if (b > c) and (d > a) and ((c+d) > (a+b)) and (c > 0) and (d > 0) and (a % 2 == 0):
        return print('Valores aceitos')
    else:
        return print('Valores nao aceitos')


def entrada():
    valores = input().split(' ')
    valor_a = int(valores[0])
    valor_b = int(valores[1])
    valor_c = int(valores[2])
    valor_d = int(valores[3])
    return valor_a, valor_b, valor_c, valor_d


n1, n2, n3, n4 = entrada()
selecao(n1, n2, n3, n4)
