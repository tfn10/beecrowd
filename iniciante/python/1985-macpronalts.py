def macpronalts():
    quantidade_de_produtos = int(input())
    precos = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }
    total = 0
    for i in range(quantidade_de_produtos):
        entrada = list(map(int, input().split()))
        numero_do_produto = entrada[0]
        quantidade_comprada = entrada[1]
        total += quantidade_comprada * precos[numero_do_produto]
    print(f'{total:.2f}')


macpronalts()
