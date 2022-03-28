def numeros_positivos():
    positivos = 0
    i = 0
    while i < 6:
        numero = float(input())
        if numero > 0:
            positivos += 1
        i += 1
    print(f'{positivos} valores positivos')


numeros_positivos()
