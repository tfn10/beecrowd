def imposto_de_renda(salario):
    if 0 <= salario <= 2000.0:
        return print('Isento')
    elif 2000.01 <= salario <= 3000.0:
        imposto_sobre_salario = imposto_de_8(salario)
    elif 3000.01 <= salario <= 4500.0:
        imposto_sobre_salario = imposto_de_18(salario)
    elif salario > 4500.00:
        imposto_sobre_salario = imposto_de_28(salario)
    return print(f'R$ {imposto_sobre_salario:.2f}')


def imposto_de_8(salario):
    imposto8 = (salario - 2000.0) * 0.08
    return imposto8


def imposto_de_18(salario):
    imposto18 = (salario - 3000.0) * 0.18 + (3000.0 - 2000.0) * 0.08
    return imposto18


def imposto_de_28(salario):
    imposto28 = (salario - 4500) * 0.28 + (4500.0 - 3000.0) * 0.18 + (3000.0 - 2000.0) * 0.08
    return imposto28


renda = float(input())
imposto_de_renda(renda)
