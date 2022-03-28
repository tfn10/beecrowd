def o_escolhido():
    quantidade_de_alunos = int(input())
    notas = list()
    numero_da_matricula = list()
    for i in range(quantidade_de_alunos):
        entrada = list(map(float, input().split()))
        numero_da_matricula.append(int(entrada[0]))
        notas.append(entrada[1])
    maior_nota = max(notas)
    if maior_nota < 8:
        print('Minimum note not reached')
    else:
        matricula_maior_nota = numero_da_matricula[notas.index(maior_nota)]
        print(matricula_maior_nota)


o_escolhido()
