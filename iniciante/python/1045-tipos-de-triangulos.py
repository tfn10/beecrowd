def entrada():
    lados = list(map(float, input().split(' ')))
    lados.sort(reverse=True)
    lado_a = lados[0]
    lado_b = lados[1]
    lado_c = lados[2]
    return lado_a, lado_b, lado_c


def tipos_triangulos(a, b, c):
    if a >= (b + c):
        print('NAO FORMA TRIANGULO')
    else:
        if (a**2) == (b**2 + c**2):
            print('TRIANGULO RETANGULO')
        elif (a**2) > (b**2 + c**2):
            print('TRIANGULO OBTUSANGULO')
        else:
            print('TRIANGULO ACUTANGULO')

        if a == b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or b == c or a == c:
            print('TRIANGULO ISOSCELES')


x1, x2, x3 = entrada()
tipos_triangulos(x1, x2, x3)
