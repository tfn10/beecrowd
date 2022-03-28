def numero_perfeito():
    numero_de_casos = int(input())
    for i in range(numero_de_casos):
        numero = int(input())
        eh_perfeito(numero)


def eh_perfeito(n):
    divisores = list()
    for j in range(1, int(n/2+1)):
        if n % j == 0:
            divisores.append(j)
    soma_divisores = sum(divisores)
    if soma_divisores == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')


numero_perfeito()
