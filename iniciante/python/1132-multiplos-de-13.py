def multiplos_de_13():
    soma = 0
    inicio = int(input())
    final = int(input())
    if inicio > final:
        inicio, final = final, inicio
    for numero in range(inicio, final+1):
        if numero % 13 != 0:
            soma += numero
    print(soma)


multiplos_de_13()
