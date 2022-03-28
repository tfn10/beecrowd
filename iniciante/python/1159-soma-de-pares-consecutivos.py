def soma_de_pares():
    while True:
        n = int(input())
        if n == 0:
            break
        if n % 2 == 0:
            soma = calculo_da_soma(n)
        else:
            n += 1
            soma = calculo_da_soma(n)
        print(soma)


def calculo_da_soma(numero):
    i = total = 0
    while i < 5:
        total += numero
        numero += 2
        i += 1
    return total


soma_de_pares()
