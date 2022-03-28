def intervalo(numero):
    valor_dentro = valor_fora = 0
    for num in range(numero):
        valor = int(input())
        if 10 <= valor <= 20:
            valor_dentro += 1
        else:
            valor_fora += 1
    return print(f'{valor_dentro} in\n'
                 f'{valor_fora} out')


n = int(input())
intervalo(n)
