def matriz_quadrada():
    while True:
        try:
            numero = int(input())
            if 5 <= numero <= 101 and numero % 2 != 0:
                matri = construindo_matriz(numero)
                imprime_matriz(matri)
        except ValueError:
            break
        except EOFError:
            break


def construindo_matriz(n):
    matriz = list()
    lin = list()
    linha_diagonal_secundaria = 0
    coluna_diagonal_secundaria = n - 1
    for linha in range(n):
        for coluna in range(n):
            if n // 2 == linha == coluna:
                lin.append(4)
            elif n // 3 <= linha <= (n - n // 3 - 1) and n // 3 <= coluna <= (n - n // 3 - 1):
                lin.append(1)
            elif linha == coluna:
                lin.append(2)
            elif linha == linha_diagonal_secundaria and coluna == coluna_diagonal_secundaria:
                lin.append(3)
            else:
                lin.append(0)
        matriz.append(lin)
        linha_diagonal_secundaria += 1
        coluna_diagonal_secundaria -= 1
        lin = list()
    return matriz


def imprime_matriz(m):
    for linha in range(len(m)):
        for coluna in range(len(m)):
            print(m[linha][coluna], end='')
        print()
    print()


matriz_quadrada()
