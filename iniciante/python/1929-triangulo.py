def triangulo():
    lados = list(map(int, input().split()))
    a = lados[0]
    b = lados[1]
    c = lados[2]
    d = lados[3]
    formam_um_triangulo = eh_triangulo(a, b, c) or \
                          eh_triangulo(a, b, d) or \
                          eh_triangulo(a, c, d) or \
                          eh_triangulo(b, c, d)
    if formam_um_triangulo:
        print('S')
    else:
        print('N')


def eh_triangulo(lado_a, lado_b, lado_c):
    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
        return True
    else:
        return False


triangulo()
