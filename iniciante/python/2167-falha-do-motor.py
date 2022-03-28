def falha_do_motor():
    velocidades = list(map(int, input().split()))
    velocidade_parametro = velocidades[0]
    posicao = 1
    for vel in velocidades[1:]:
        if velocidade_parametro > vel:
            return posicao + 1
        posicao += 1
        velocidade_parametro = vel
    return 0


def main():
    n = int(input())
    pos = falha_do_motor()
    print(pos)


main()
