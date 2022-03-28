def estagio():
    numero_de_disciplina = int(input())
    soma_nota_x_carga_horaria = 0
    carga_horaria_total = 0
    for i in range(numero_de_disciplina):
        entrada = list(map(int, input().split()))
        nota = entrada[0]
        carga_horaria = entrada[1]
        soma_nota_x_carga_horaria += nota * carga_horaria
        carga_horaria_total += carga_horaria
    ira = float((1000 * soma_nota_x_carga_horaria) / (1000 * (carga_horaria_total * 100)))
    print(f'{ira:.4f}')


estagio()
