def area_direita():
    operacao = input()
    matriz = list()
    linha = list()
    total = 0
    numero_de_celulas = 0
    count1 = 11
    count2 = 7

    # Coloca os valores em cada célula da matriz 12x12
    for i in range(12):
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        linha = list()

    # Soma todos os valores da área direita da matriz:
    for k in range(1, 6):
        for m in range(7, 12):
            if m >= count1:
                total += matriz[k][m]
        count1 -= 1
    for n in range(6, 12):
        for o in range(7, 12):
            if o >= count2:
                total += matriz[n][o]
        count2 += 1

    # imprime o total ou média da área direita da matriz
    if operacao == 'S':
        print(f'{total:.1f}')
    elif operacao == 'M':
        media = total / numero_de_celulas
        print(f'{media:.1f}')


area_direita()
