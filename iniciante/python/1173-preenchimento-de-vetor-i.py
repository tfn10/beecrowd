def preenchimento_de_vetor():
    numero = int(input())
    valores = list()
    valores.append(numero)
    for i in range(9):
        numero *= 2
        valores.append(numero)
    for j in range(10):
        print(f'N[{j}] = {valores[j]}')


preenchimento_de_vetor()
