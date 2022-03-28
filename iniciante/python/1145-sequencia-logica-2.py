def sequencia_logica():
    coluna, numero_final = entrada()
    for num in range(1, numero_final+1):
        if num % coluna == 0:
            print(num)
        else:
            if num == numero_final:
                print(num)
            else:
                print(f'{num}', end=' ')


def entrada():
    valores = list(map(int, input().split(' ')))
    x = valores[0]
    y = valores[1]
    return x, y


sequencia_logica()
