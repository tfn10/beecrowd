def pares(num):
    valores_pares = 0
    for n in num:
        if n % 2 == 0:
            valores_pares += 1
    return print(f'{valores_pares} valor(es) par(es)')


def impares(num):
    valores_impares = 0
    for n in num:
        if n % 2 != 0:
            valores_impares += 1
    return print(f'{valores_impares} valor(es) impar(es)')


def positivos(num):
    valores_positivos = 0
    for n in num:
        if n > 0:
            valores_positivos += 1
    return print(f'{valores_positivos} valor(es) positivo(s)')


def negativos(num):
    valores_negativos = 0
    for n in num:
        if n < 0:
            valores_negativos += 1
    return print(f'{valores_negativos} valor(es) negativo(s)')


def entrada():
    numeros = list()
    for i in range(5):
        numeros.append(int(input()))
    return numeros


numbers = entrada()
pares(numbers)
impares(numbers)
positivos(numbers)
negativos(numbers)
