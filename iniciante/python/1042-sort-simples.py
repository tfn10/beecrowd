def sort_simples():
    numeros = input().split(' ')
    numeros = list(map(int, numeros))
    numeros_ordenados = sorted(numeros)
    for num in numeros_ordenados:
        print(num)
    print()
    for n in numeros:
        print(n)


sort_simples()
