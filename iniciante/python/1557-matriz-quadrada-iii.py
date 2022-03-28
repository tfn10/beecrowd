def matriz_quadrada():
    while True:
        n = int(input())
        if n == 0:
            break
        matriz = list()
        linha = list()
        for i in range(n):
            valor = 2 ** i
            for j in range(n):
                linha.append(valor)
                valor = valor * 2
            matriz.append(linha)
            linha = list()
        imprime_matriz(matriz)


def imprime_matriz(m):
    maiores_valores_linha = list()
    for i in range(len(m)):
        maiores_valores_linha.append(max(m[i]))
    maior_valor_matriz = max(maiores_valores_linha)
    algarismos_do_maior = len(str(maior_valor_matriz))
    for linha in range(len(m)):
        for coluna in range(len(m)):
            if coluna == 0:
                print(f'{m[linha][coluna]}'.rjust(algarismos_do_maior), end='')
            else:
                print(f'{m[linha][coluna]}'.rjust(algarismos_do_maior+1), end='')
        print()


matriz_quadrada()
