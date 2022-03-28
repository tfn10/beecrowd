def preenchimento_de_vetor():
    vetor = list()
    t = int(input())
    for i in range(1000):
        for j in range(t):
            vetor.append(j)
    for k in range(1000):
        print(f'N[{k}] = {vetor[k]}')


preenchimento_de_vetor()
