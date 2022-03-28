def numeros_positivos():
    positivos = soma = i = 0
    while i < 6:
        numero = float(input())
        if numero > 0:
            positivos += 1
            soma += numero
        i += 1
    media = soma / positivos
    print(f'{positivos} valores positivos')
    print(f'{media:.1f}')


numeros_positivos()
