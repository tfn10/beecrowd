def aumento_salario(salario):
    if 0.0 <= salario <= 400.0:
        porcentagem = 0.15
        reajuste_ganho = porcentagem * salario
        novo_salario = salario + reajuste_ganho
    elif 400.01 <= salario <= 800.0:
        porcentagem = 0.12
        reajuste_ganho = porcentagem * salario
        novo_salario = salario + reajuste_ganho
    elif 800.01 <= salario <= 1200.0:
        porcentagem = 0.10
        reajuste_ganho = porcentagem * salario
        novo_salario = salario + reajuste_ganho
    elif 1200.01 <= salario <= 2000.0:
        porcentagem = 0.07
        reajuste_ganho = porcentagem * salario
        novo_salario = salario + reajuste_ganho
    elif salario > 2000.0:
        porcentagem = 0.04
        reajuste_ganho = porcentagem * salario
        novo_salario = salario + reajuste_ganho
    return print(f'Novo salario: {novo_salario:.2f}\n'
                 f'Reajuste ganho: {reajuste_ganho:.2f}\n'
                 f'Em percentual: {int(porcentagem * 100)} %')


valor_salario = float(input())
aumento_salario(valor_salario)
