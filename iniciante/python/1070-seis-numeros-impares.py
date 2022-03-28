def seis_numeros_impares(num):
    numeros_impares = 0
    while True:
        if num % 2 != 0:
            numeros_impares += 1
            print(num)
        if numeros_impares == 6:
            break
        num += 1


numero = int(input())
seis_numeros_impares(numero)
