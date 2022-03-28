def ultimo_analogimon():
    while True:
        try:
            entrada = list(map(int, input().split()))
            numero_de_linhas = entrada[0]
            numero_de_colunas = entrada[1]
            matrix, analogimon_posicao, posicao_sua = construindo_a_matriz(numero_de_linhas)
            print(tempo_gasto(analogimon_posicao, posicao_sua))
        except EOFError:
            break
        except IndexError:
            break
        except ValueError:
            break


def construindo_a_matriz(n_linhas):
    matriz = list()
    aux = list()
    for linha in range(n_linhas):
        valores_da_linha = list(map(int, input().split()))
        if 2 in valores_da_linha:
            posicao_coluna_analoginom = valores_da_linha.index(2)
            posicao_linha_analoginom = linha
        if 1 in valores_da_linha:
            sua_posicao_coluna = valores_da_linha.index(1)
            sua_posicao_linha = linha
        aux.append(valores_da_linha)
        matriz.append(aux)
        aux = list()
    posicao_analoginom = [posicao_linha_analoginom, posicao_coluna_analoginom]
    sua_posicao = [sua_posicao_linha, sua_posicao_coluna]
    return matriz, posicao_analoginom, sua_posicao


def tempo_gasto(posicao_analoginom, sua_posicao):
    linha_posicao_analoginom = posicao_analoginom[0]
    coluna_posicao_analoginom = posicao_analoginom[1]
    linha_posicao_voce = sua_posicao[0]
    coluna_posicao_voce = sua_posicao[1]
    diferenca_de_linha = abs(linha_posicao_analoginom-linha_posicao_voce)
    diferenca_de_coluna = abs(coluna_posicao_analoginom-coluna_posicao_voce)
    tempo_total_gasto = diferenca_de_coluna + diferenca_de_linha
    return tempo_total_gasto


ultimo_analogimon()
