def calculo_peca():
    produto = input().split(' ')
    codigo = int(produto[0])
    numero_pecas = int(produto[1])
    valor_unitario = float(produto[2])
    valor_das_pecas = numero_pecas * valor_unitario
    return valor_das_pecas


peca1 = calculo_peca()
peca2 = calculo_peca()
valor_pagar = peca1 + peca2
print(f'VALOR A PAGAR: R$ {valor_pagar:.2f}')
