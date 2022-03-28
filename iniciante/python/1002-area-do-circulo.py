def area_do_circulo(r):
    # PI = 3.14159
    area = (r ** 2) * 3.14159
    return print(f'A={area:.4f}')


raio = float(input())
area_do_circulo(raio)
