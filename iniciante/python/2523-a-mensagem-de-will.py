def mensagem_de_will():
    while True:
        try:
            string = input().upper()
            lampadas_piscadas = int(input())
            numero_lampada_piscada = list(map(int, input().split()))
            for posicao in numero_lampada_piscada:
                print(string[posicao-1], end='')
            print()
        except EOFError:
            break
        except ValueError:
            break


mensagem_de_will()
