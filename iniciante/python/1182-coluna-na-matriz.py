def coluna_na_matriz():
    numero_da_coluna = int(input())
    operacao = input()
    matriz = list()
    linha = list()
    coluna_escolhida = list()
    for i in range(12):
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        linha = list()
    for k in range(12):
        coluna_escolhida.append(matriz[k][numero_da_coluna])
    if operacao == 'S':
        soma = sum(coluna_escolhida)
        print(f'{soma:.1f}')
    elif operacao == 'M':
        media = sum(coluna_escolhida)/len(coluna_escolhida)
        print(f'{media:.1f}')


coluna_na_matriz()
