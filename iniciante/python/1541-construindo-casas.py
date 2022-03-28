def construindo_casas():
    while True:
        try:
            numeros = list(map(int, input().split()))
            a = numeros[0]
            b = numeros[1]
            c = numeros[2]
            if a == 0 or b == 0 or c == 0:
                break
            lado_do_terreno = 0
            area_da_casa = a * b
            percentual_maximo = c / 100
            while True:
                if (lado_do_terreno ** 2) * percentual_maximo == area_da_casa:
                    break
                elif (lado_do_terreno ** 2) * percentual_maximo > area_da_casa:
                    lado_do_terreno -= 1
                    break
                lado_do_terreno += 1
            print(lado_do_terreno)
        except IndexError:
            break


construindo_casas()
