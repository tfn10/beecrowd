def salario(vendedor, salario_fixo, total_vendas):
    comissao_ganha = total_vendas * 0.15
    salario_total = comissao_ganha + salario_fixo
    return print(f'TOTAL = R$ {salario_total:.2f}')


nome_vendendor = input()
sal_fixo = float(input())
vendas_total = float(input())

salario(nome_vendendor, sal_fixo, vendas_total)
