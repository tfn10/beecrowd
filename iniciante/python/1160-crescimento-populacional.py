def entrada():
    valores = input().split(' ')
    populacao_cidade_a = int(valores[0])
    populacao_cidade_b = int(valores[1])
    crescimento_cidade_a = float(valores[2])
    crescimento_cidade_b = float(valores[3])
    return populacao_cidade_a, populacao_cidade_b, crescimento_cidade_a, crescimento_cidade_b


def crescimento_populacional(n):
    for i in range(n):
        pa, pb, ga, gb = entrada()
        anos = 0
        while True:
            pa = int(pa*(1+(ga/100)))
            pb = int(pb*(1+(gb/100)))
            anos += 1
            if pa > pb or anos > 100:
                break
        if anos > 100:
            print('Mais de 1 seculo.')
        else:
            print(f'{anos} anos.')


numero_de_testes = int(input())
crescimento_populacional(numero_de_testes)
