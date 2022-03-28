def selecao_em_vetor():
    vetor = list()
    for i in range(100):
        vetor.append(float(input()))
    for j in range(100):
        if vetor[j] <= 10.0:
            print(f'A[{j}] = {vetor[j]:.1f}')


selecao_em_vetor()
