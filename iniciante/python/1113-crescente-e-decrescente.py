def crescente_e_decrescente():
    while True:
        n1, n2 = entrada()
        if n1 > n2:
            print('Decrescente')
        elif n1 < n2:
            print('Crescente')
        else:
            break


def entrada():
    numeros = list(map(int, input().split(' ')))
    numero1 = numeros[0]
    numero2 = numeros[1]
    return numero1, numero2


crescente_e_decrescente()
