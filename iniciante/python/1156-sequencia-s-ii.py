def sequencia():
    numerador = 1
    exponencial = s = 0
    fator = 2
    while True:
        s += (numerador/(fator ** exponencial))
        if numerador == 39:
            break
        numerador += fator
        exponencial += 1
    print(f'{s:.2f}')


sequencia()
