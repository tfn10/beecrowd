def bob_conduite():
    numero_de_testes = int(input())
    while numero_de_testes > 0:
        raios = list(map(int, input().split()))
        r1 = raios[0]
        r2 = raios[1]
        print(r1+r2)
        numero_de_testes -= 1


bob_conduite()
