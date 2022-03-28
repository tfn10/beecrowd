def matriz_quadrada():
    while True:
        n = int(input())
        if n == 0:
            break
        elif n == 1:
            print(f'{n}'.rjust(3))
        else:
            matriz = list()
            linha = list()
            for i in range(n):
                for j in range(n):
                    linha.append(abs(i - j) + 1)
                matriz.append(linha)
                linha = list()
            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    print(f'{matriz[i][j]}'.rjust(3), end='')
                print()


matriz_quadrada()
