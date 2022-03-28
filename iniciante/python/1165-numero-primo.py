def numero_primo():
    numero_de_casos = int(input())
    for i in range(numero_de_casos):
        numero = int(input())
        eh_primo(numero)


def eh_primo(n):
    if n == 1:
        return print(f'{n} nao eh primo')
    elif n == 2:
        return print(f'{n} eh primo')
    for j in range(2, int(n/2+1)):
        if n % j == 0:
            return print(f'{n} nao eh primo')
    return print(f'{n} eh primo')


numero_primo()
