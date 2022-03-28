def entrada():
    numeros = list(map(int, input().split(' ')))
    n1 = numeros[0]
    n2 = numeros[1]
    return n1, n2


def soma_de_impares_consecutivos(quantidade_de_testes):
    while quantidade_de_testes > 0:
        x, y = entrada()
        if x > y:
            x, y = y, x
        soma = 0
        for i in range(x+1, y):
            if i % 2 != 0:
                soma += i
        print(soma)
        quantidade_de_testes -= 1


quant_de_testes = int(input())
soma_de_impares_consecutivos(quant_de_testes)
