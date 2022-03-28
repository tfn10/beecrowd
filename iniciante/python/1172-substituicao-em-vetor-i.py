def substituicao_em_vetor():
    vetor = list()
    for i in range(10):
        numero = int(input())
        vetor.append(numero)
        if vetor[i] <= 0:
            vetor[i] = 1
    for j in range(10):
        print(f'X[{j}] = {vetor[j]}')


substituicao_em_vetor()
