def corrida_de_lesmas():
    while True:
        try:
            numeros_de_testes = int(input())
            testes = list(map(int, input().split()))
            maior_velocidade = max(testes)
            if maior_velocidade < 10:
                nivel = 1
            elif 10 <= maior_velocidade < 20:
                nivel = 2
            elif maior_velocidade >= 20:
                nivel = 3
            print(nivel)
        except EOFError:
            break
        except ValueError:
            break


corrida_de_lesmas()
