def entrada():
    numeros = list(map(float, input().split(' ')))
    n1 = numeros[0]
    n2 = numeros[1]
    n3 = numeros[2]
    return n1, n2, n3


def media(num1, num2, num3):
    media_ponderada = (num1 * 2 + num2 * 3 + num3 * 5) / 10
    return print(f'{media_ponderada:.1f}')


def calculo_da_media(tentativas):
    for i in range(tentativas):
        x1, x2, x3 = entrada()
        media(x1, x2, x3)


numero_de_tentativas = int(input())
calculo_da_media(numero_de_tentativas)
