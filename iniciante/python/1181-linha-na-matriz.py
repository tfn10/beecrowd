def linha_na_matriz():
    numero_da_linha = int(input())
    operacao = input()
    matriz = list()
    linha = list()
    for i in range(12):
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        linha = list()
    if operacao == 'S':
        soma = sum(matriz[numero_da_linha])
        print(f'{soma:.1f}')
    elif operacao == 'M':
        media = sum(matriz[numero_da_linha])/len(matriz[numero_da_linha])
        print(f'{media:.1f}')


linha_na_matriz()
