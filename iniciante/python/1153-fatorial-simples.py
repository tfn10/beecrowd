def fatorial_simples():
    n = int(input())
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    print(fatorial)


fatorial_simples()
