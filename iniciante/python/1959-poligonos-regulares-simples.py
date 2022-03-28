def poligonos_regulares_simples():
    entrada = list(map(int, input().split()))
    numero_de_lados = entrada[0]
    comprimento_de_cada_lado = entrada[1]
    perimetro = numero_de_lados * comprimento_de_cada_lado
    print(perimetro)


poligonos_regulares_simples()
