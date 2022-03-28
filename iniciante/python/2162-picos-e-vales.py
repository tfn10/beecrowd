def picos_e_vales():
    n = int(input())
    alturas = list(map(int, input().split()))
    referencia1 = alturas[0]
    referencia2 = alturas[1]
    if referencia1 > referencia2:
        for i in range(2, n):
            if i % 2 == 0:
                if referencia2 >= alturas[i]:
                    return 0
            else:
                if referencia2 <= alturas[i]:
                    return 0
            referencia2 = alturas[i]
    elif referencia1 < referencia2:
        for j in range(2, n):
            if j % 2 == 0:
                if referencia2 <= alturas[j]:
                    return 0
            else:
                if referencia2 >= alturas[j]:
                    return 0
            referencia2 = alturas[j]
    else:
        return 0
    return 1


resultado = picos_e_vales()
print(resultado)
