def conta():
    numero_de_teste = int(input())
    for i in range(numero_de_teste):
        n = int(input())
        if n % 2 == 0:
            print(0)
        else:
            print(1)


conta()
