def somando_inteiros_consecutivos():
    a, n = entrada()
    soma = 0
    for i in range(n):
        soma = soma + a + i
    print(soma)


def entrada():
    valores = list(map(int, input().split()))
    valor_de_a = valores[0]
    valor_de_n = valores[len(valores) - 1]
    return valor_de_a, valor_de_n


somando_inteiros_consecutivos()
