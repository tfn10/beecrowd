def qual_triangulo():
    valores = list(map(int, input().split()))
    lado_a = valores[0]
    lado_b = valores[1]
    lado_c = valores[2]
    if eh_triangulo(lado_a, lado_b, lado_c):
        print('Valido-', end='')
        tipo_de_triangulo(lado_a, lado_b, lado_c)
        eh_triangulo_retangulo(lado_a, lado_b, lado_c)
    else:
        print('Invalido')


def eh_triangulo(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


def tipo_de_triangulo(a, b, c):
    if a == b == c:
        print('Equilatero')
    elif a != b and a != c and b != c:
        print('Escaleno')
    else:
        print('Isoceles')


def eh_triangulo_retangulo(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 or \
            a ** 2 + c ** 2 == b ** 2 or \
            b ** 2 + c ** 2 == a ** 2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')


qual_triangulo()
