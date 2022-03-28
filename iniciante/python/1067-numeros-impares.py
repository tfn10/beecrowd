def numeros_impares(num):
    for n in range(num+1):
        if n % 2 != 0:
            print(n)


numeros = int(input())
numeros_impares(numeros)
