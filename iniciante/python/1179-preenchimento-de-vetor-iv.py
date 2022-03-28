def preenchimento_de_vetor_iv():
    n = 0
    par = list()
    impar = list()
    while n < 15:
        numero = int(input())
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
        if len(par) == 5:
            for i in range(5):
                print(f'par[{i}] = {par[i]}')
            par = list()
        elif len(impar) == 5:
            for j in range(5):
                print(f'impar[{j}] = {impar[j]}')
            impar = list()
        n += 1
    for k in range(len(impar)):
        print(f'impar[{k}] = {impar[k]}')
    for t in range(len(par)):
        print(f'par[{t}] = {par[t]}')


preenchimento_de_vetor_iv()
