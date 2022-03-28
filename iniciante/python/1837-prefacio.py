def prefacio():
    valores = list(map(int, input().split()))
    a = valores[0]
    b = valores[1]
    quociente = resto = 0
    if b < 0:
        if a > 0:
            quociente = -(a // (-b))
            resto = a - (b * quociente)
        elif a < 0:
            quociente = (-a) // (-b)
            resto = a - b * quociente
    else:
        quociente = a // b
        resto = a % b
    print(f'{quociente} {resto}')


prefacio()
