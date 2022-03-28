def evento():
    while True:
        valores = list(map(int, input().split()))
        valor1 = valores[0]
        valor2 = valores[1]
        if valor1 == valor2 == 0:
            break
        print(valor1 * valor2)


evento()
