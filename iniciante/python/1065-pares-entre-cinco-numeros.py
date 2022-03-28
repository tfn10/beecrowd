def pares():
    valores_pares = i = 0
    while i < 5:
        numero = int(input())
        if numero % 2 == 0:
            valores_pares += 1
        i += 1
    print(f'{valores_pares} valores pares')


pares()
