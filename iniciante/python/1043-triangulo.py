def entrada():
    lados = input().split(' ')
    lados = list(map(float, lados))
    lado_a = lados[0]
    lado_b = lados[1]
    lado_c = lados[2]
    return lado_a, lado_b, lado_c


def area_ou_perimetro(a, b, c):
    # calcula o perímetro do triângulo
    if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
        perimetro_triangulo = a + b + c
        return print(f'Perimetro = {perimetro_triangulo:.1f}')

    # calcula a área do trapézio
    else:
        area_trapezio = ((a+b) * c)/2
        return print(f'Area = {area_trapezio:.1f}')


x1, x2, x3 = entrada()
area_ou_perimetro(x1, x2, x3)
