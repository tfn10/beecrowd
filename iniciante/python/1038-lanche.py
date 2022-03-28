def lanche(codigo, unidade):
    precos = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
    total = precos[codigo] * unidade
    return print(f'Total: R$ {total:.2f}')


def entrada():
    codigos = input().split(' ')
    prod = int(codigos[0])
    unidades = int(codigos[1])
    return prod, unidades


produto, quantidade = entrada()
lanche(produto, quantidade)
