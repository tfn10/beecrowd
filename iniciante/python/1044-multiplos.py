def multiplos():
    valores = list(map(int, input().split(' ')))
    a = valores[0]
    b = valores[1]
    if b % a == 0 or a % b == 0:
        return print('Sao Multiplos')
    else:
        return print('Nao sao Multiplos')


multiplos()
