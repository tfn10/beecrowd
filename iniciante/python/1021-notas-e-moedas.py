def cedulas(n):
    print('NOTAS:')
    notas = [100000, 50000, 20000, 10000, 5000, 2000]
    restante = n * 1000
    for nota in notas:
        quantidade_cedula = restante // nota
        restante = restante % nota
        print(f'{int(quantidade_cedula)} nota(s) de R$ {(nota/1000):.2f}')
    moedas(restante/1000)


def moedas(n):
    print('MOEDAS:')
    cents = [1000, 500, 250, 100, 50, 10]
    resto = n * 1000
    for cent in cents:
        quantidade_moeda = resto // cent
        resto = resto % cent
        print(f'{int(quantidade_moeda)} moeda(s) de R$ {(cent/1000):.2f}')


cel = float(input())
cedulas(cel)
