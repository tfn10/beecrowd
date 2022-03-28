def c_mais_ou_menos():
    quantidade_de_vitamina_c_nos_alimentos = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis': 34
    }
    while True:
        total_de_vitamina_c = 0
        quantidade_de_alimentos_consumido = int(input())
        if quantidade_de_alimentos_consumido == 0:
            break
        for i in range(quantidade_de_alimentos_consumido):
            nome_e_quantidade_do_alimento = list(map(str, input().split()))
            quantidade_de_alimento = int(nome_e_quantidade_do_alimento[0])
            nome_do_alimento = ' '.join(nome_e_quantidade_do_alimento[1:])
            total_de_vitamina_c += (quantidade_de_alimento * quantidade_de_vitamina_c_nos_alimentos[nome_do_alimento])
        if 110 <= total_de_vitamina_c <= 130:
            print(f'{total_de_vitamina_c} mg')
        elif total_de_vitamina_c < 110:
            print(f'Mais {110 - total_de_vitamina_c} mg')
        else:
            print(f'Menos {total_de_vitamina_c - 130} mg')


c_mais_ou_menos()
