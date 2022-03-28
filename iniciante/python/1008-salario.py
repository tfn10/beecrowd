def salario(numero_de_funcionarios, horas_trabalhadas, valor_por_hora):
    salary = horas_trabalhadas * valor_por_hora
    saida = f'NUMBER = {numero_de_funcionarios}\n' \
            f'SALARY = U$ {salary:.2f}'
    return print(saida)


n_funcionarios = int(input())
hrs_trabalhadas = int(input())
valor_hora = float(input())
salario(n_funcionarios, hrs_trabalhadas, valor_hora)
