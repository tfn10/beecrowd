def valor_de_xz():
    valor_de_x = int(input())
    while True:
        valor_de_z = int(input())
        if valor_de_z > valor_de_x:
            break
    return valor_de_x, valor_de_z


def soma_dos_valores():
    x, y = valor_de_xz()
    soma = 0
    quantidade_de_numeros = 0
    while True:
        soma += x
        x += 1
        quantidade_de_numeros += 1
        if soma > y:
            break
    print(quantidade_de_numeros)


soma_dos_valores()
