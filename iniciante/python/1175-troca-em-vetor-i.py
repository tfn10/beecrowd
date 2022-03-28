def troca_em_vetor():
    vetor = list()
    for i in range(20):
        vetor.append(int(input()))
    vetor_inverso = vetor[::-1]
    for j in range(20):
        print(f'N[{j}] = {vetor_inverso[j]}')


troca_em_vetor()
