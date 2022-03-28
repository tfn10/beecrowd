def desafio_de_bino():
    n = int(input())
    valores = list(map(int, input().split()))
    multiplos_de_2 = 0
    multiplos_de_3 = 0
    multiplos_de_4 = 0
    multiplos_de_5 = 0
    for numero in valores:
        if numero % 2 == 0:
            multiplos_de_2 += 1
        if numero % 3 == 0:
            multiplos_de_3 += 1
        if numero % 4 == 0:
            multiplos_de_4 += 1
        if numero % 5 == 0:
            multiplos_de_5 += 1
    print(f'{multiplos_de_2} Multiplo(s) de 2\n'
          f'{multiplos_de_3} Multiplo(s) de 3\n'
          f'{multiplos_de_4} Multiplo(s) de 4\n'
          f'{multiplos_de_5} Multiplo(s) de 5')


desafio_de_bino()
