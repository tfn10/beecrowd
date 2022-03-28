def resto_2(num):
    for i in range(1, 10001):
        if i % num == 2:
            print(i)


numero = int(input())
resto_2(numero)
