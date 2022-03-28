def menor_e_posicao():
    lista_de_valores = entrada()
    valor_minimo = min(lista_de_valores)
    posicao = lista_de_valores.index(valor_minimo)
    print(f'Menor valor: {valor_minimo}\n'
          f'Posicao: {posicao}')


def entrada():
    n = int(input())
    valores = list(map(int, input().split()))
    return valores


menor_e_posicao()
