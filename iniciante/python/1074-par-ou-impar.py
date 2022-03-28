def entrada(numero):
    n = list()
    for num in range(numero):
        n.append(int(input()))
    return n


def par_ou_impar(valores):
    for valor in valores:
        if valor == 0:
            print('NULL')
        else:
            if valor % 2 == 0:
                print('EVEN', end=' ')
            else:
                print('ODD', end=' ')
            if valor > 0:
                print('POSITIVE')
            else:
                print('NEGATIVE')


number = entrada(int(input()))
par_ou_impar(number)
