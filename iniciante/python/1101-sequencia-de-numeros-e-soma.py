def entrada():
    numeros = list(map(int, input().split(' ')))
    numero1 = numeros[0]
    numero2 = numeros[1]
    return numero1, numero2


def sequencia_de_numeros_e_soma():
    while True:
        lista_sequencia_de_numeros = list()
        n1, n2 = entrada()
        if n1 <= 0 or n2 <= 0:
            break
        if n1 > n2:
            n1, n2 = n2, n1
        for num in range(n1, n2+1):
            lista_sequencia_de_numeros.append(num)
            print(num, end=' ')
        print(f'Sum={sum(lista_sequencia_de_numeros)}')


sequencia_de_numeros_e_soma()
