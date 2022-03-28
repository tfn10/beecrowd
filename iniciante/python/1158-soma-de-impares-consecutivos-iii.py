def soma_de_impares(n):
    for i in range(n):
        x, y = entrada()
        if x % 2 != 0:
            soma = calculo_da_soma(x, y)
        else:
            x += 1
            soma = calculo_da_soma(x, y)
        print(soma)


def calculo_da_soma(valor_x, valor_y):
    total = 0
    while valor_y > 0:
        total += valor_x
        valor_x += 2
        valor_y -= 1
    return total


def entrada():
    valores = list(map(int, input().split(' ')))
    valor_de_x = valores[0]
    valor_de_y = valores[1]
    return valor_de_x, valor_de_y


numero_de_testes = int(input())
soma_de_impares(numero_de_testes)
