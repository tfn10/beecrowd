def matriz_123():
    while True:
        try:
            n = int(input())
            if 3 <= n <= 70:
                matri = construindo_matriz(n)
                imprime_matriz(matri)
            else:
                break
        except EOFError:
            break
        except ValueError:
            break


def construindo_matriz(numero):
    matriz = list()
    linha = list()
    linha_diagonal_secundaria = 0
    coluna_diagonal_secundaria = numero - 1
    if numero % 2 == 0:
        for i in range(numero):
            for j in range(numero):
                if i == j:
                    linha.append(1)
                elif i == linha_diagonal_secundaria and j == coluna_diagonal_secundaria:
                    linha.append(2)
                else:
                    linha.append(3)
            matriz.append(linha)
            linha_diagonal_secundaria += 1
            coluna_diagonal_secundaria -= 1
            linha = list()
    else:
        for i in range(numero):
            for j in range(numero):
                if i == linha_diagonal_secundaria and j == coluna_diagonal_secundaria:
                    linha.append(2)
                elif i == j:
                    linha.append(1)
                else:
                    linha.append(3)
            matriz.append(linha)
            linha_diagonal_secundaria += 1
            coluna_diagonal_secundaria -= 1
            linha = list()
    return matriz


def imprime_matriz(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end='')
        print()


matriz_123()
