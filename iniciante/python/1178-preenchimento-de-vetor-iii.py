def preenchimento_de_vetor():
    x = float(input())
    x = int(x)
    vetor = list()
    for i in range(100):
        vetor.append(x)
        print(f'N[{i}] = {(vetor[i]):.4f}')
        x = x/2


preenchimento_de_vetor()
