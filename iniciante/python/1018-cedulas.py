def entrada_valida():
    numero = int(input())
    if numero <= 0 or numero >= 1000000:
        while True:
            numero = int(input())
            if 0 < numero < 1000000:
                break
    return numero


def cedulas(n):
    print(n)
    notas = [100, 50, 20, 10, 5, 2, 1]
    restante = n
    for nota in notas:
        cedula = restante // nota
        restante -= cedula * nota
        print(f'{cedula} nota(s) de R$ {nota},00')


cel = entrada_valida()
cedulas(cel)
