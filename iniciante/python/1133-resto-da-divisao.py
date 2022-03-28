def resto_da_divisao():
    inicio = int(input())
    final = int(input())
    if inicio > final:
        inicio, final = final, inicio
    for numero in range(inicio+1, final):
        if numero % 5 == 2 or numero % 5 == 3:
            print(numero)


resto_da_divisao()
