def acima_da_diagonal_principal():
    operacao = input()
    matriz = list()
    linha = list()
    total = 0
    numero_de_celulas = 0
    aux = 0
    for i in range(12):
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        linha = list()
    for k in range(12):
        for t in range(12):
            if t > aux:
                total += matriz[k][t]
                numero_de_celulas += 1
        aux += 1
    if operacao == 'S':
        print(f'{total:.1f}')
    elif operacao == 'M':
        media = total / numero_de_celulas
        print(f'{media:.1f}')


acima_da_diagonal_principal()
