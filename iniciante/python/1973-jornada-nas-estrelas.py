def main():
    from sys import stdin
    n = int(stdin.readline())
    estrelas = list(map(int, stdin.readline().split()))
    total_de_carneiros = sum(estrelas)
    i = 0
    estrelas_atacadas = list()
    carneiros_roubados = 0
    while 0 <= i < n:
        if i not in estrelas_atacadas:
            estrelas_atacadas.append(i)
        if estrelas[i] % 2 != 0:
            if estrelas[i] > 0:
                carneiros_roubados += 1
                estrelas[i] -= 1
            i += 1
        else:
            if estrelas[i] > 0:
                carneiros_roubados += 1
                estrelas[i] -= 1
            i -= 1
    carneiros_nao_roubados = total_de_carneiros - carneiros_roubados
    print(f'{len(estrelas_atacadas)} {carneiros_nao_roubados}')


if __name__ == "__main__":
    main()
