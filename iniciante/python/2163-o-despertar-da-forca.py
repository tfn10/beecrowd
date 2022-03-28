def matrix():
    valores = list(map(int, input().split()))
    num_linha = valores[0]
    m = list()
    for lin in range(num_linha):
        linha = list(map(int, input().split()))
        m.append(linha)
    return m


def posicao_do_42(matriz):
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    pos_42 = list()
    for lin in range(n_linha):
        for col in range(n_coluna):
            if matriz[lin][col] == 42:
                pos_42.append([lin, col])
    return pos_42


def despertar_da_forca(matriz, posicoes_do_num_42):
    for pos in posicoes_do_num_42:
        numero_da_linha = pos[0]
        numero_da_coluna = pos[1]
        quantidade_de_7 = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i != 0 and j != 0:
                    if matriz[numero_da_coluna+i][numero_da_linha+j] == 7:
                        quantidade_de_7 += 1
        if quantidade_de_7 == 8:
            return [numero_da_linha, numero_da_coluna]
    return [0, 0]


def main():
    ma = matrix()
    posicao_42 = posicao_do_42(ma)
    resultado = despertar_da_forca(ma, posicao_42)
    print(f'{resultado[0]} {resultado[1]}')

main()
"""def teste_main():
    matriz1 = [[11, 12, 7, 7, 7, 13, 14],
               [15, 6, 7, 42, 7, 7, 42],
               [98, -5, 7, 7, 7, 42, 7],
               [-1, 42, 3, 9, 7, 7, 7]]
    matriz2 = [[11, 12, 7, 7, 7, 13, 14],
               [15, 6, 7, 12, 7, 7, 42],
               [98, -5, 7, 7, 7, 42, 7],
               [-1, 42, 3, 9, 7, 7, 7]]
    matriz3 = [[7, 7, 7],
               [7, 42, 7],
               [7, 7, 7]]
    pos42_matriz1 = posicao_do_42(matriz1)
    pos42_matriz2 = posicao_do_42(matriz2)
    pos42_matriz3 = posicao_do_42(matriz3)

    teste_matriz1 = despertar_da_forca(matriz1, pos42_matriz1)
    teste_matriz2 = despertar_da_forca(matriz2, pos42_matriz2)
    teste_matriz3 = despertar_da_forca(matriz3, pos42_matriz3)

    if teste_matriz1 == [2, 4]\
            and teste_matriz2 == [0, 0]\
            and teste_matriz3 == [2, 2]:
        print('Nenhum erro!!! :)')
"""