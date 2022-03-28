def entrada():
    numeros = list(map(int, input().split(' ')))
    n1 = numeros[0]
    n2 = numeros[1]
    return n1, n2


def dividindo(n):
    for i in range(n):
        dividendo, divisor = entrada()
        if divisor == 0:
            print('divisao impossivel')
        else:
            divisao = dividendo / divisor
            print(f'{divisao:.1f}')


numero_de_vezes = int(input())
dividindo(numero_de_vezes)
