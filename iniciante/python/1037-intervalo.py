def intervalo(numero):
    if 0 <= numero <= 25:
        return print('Intervalo [0,25]')
    elif 25 < numero <= 50:
        return print('Intervalo (25,50]')
    elif 50 < numero <= 75:
        return print('Intervalo (50,75]')
    elif 75 < numero <= 100:
        return print('Intervalo (75,100]')
    else:
        return print('Fora de intervalo')


n = float(input())
intervalo(n)
