def maior_de_dois(numero1, numero2):
    maior = int((numero1 + numero2 + abs(numero1-numero2))/2)
    return maior


def entrada():
    numeros = input().split(' ')
    a = int(numeros[0])
    b = int(numeros[1])
    c = int(numeros[2])
    return a, b, c


def maior_de_tres(a, b, c):
    if a >= c:
        maior_numero = maior_de_dois(a, c)
    else:
        maior_numero = maior_de_dois(b, c)
    return print(f'{maior_numero} eh o maior')


n1, n2, n3 = entrada()
maior_de_tres(n1, n2, n3)
