def area_inferior():
    operacao = input()
    matriz = list()
    linha = list()
    total = 0
    intervalo1 = 5
    intervalo2 = 6
    numero_de_celulas = 0
    for i in range(12):
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        linha = list()
    for k in range(7, 12):
        for t in range(12):
            if intervalo1 <= t <= intervalo2:
                total += matriz[k][t]
                numero_de_celulas += 1
        intervalo1 -= 1
        intervalo2 += 1

    if operacao == 'S':
        print(f'{total:.1f}')
    elif operacao == 'M':
        media = total / numero_de_celulas
        print(f'{media:.1f}')


area_inferior()
