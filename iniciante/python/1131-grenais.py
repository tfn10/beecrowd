def entrada():
    placar_grenal = list(map(int, input().split(' ')))
    inter = placar_grenal[0]
    gre = placar_grenal[1]
    return inter, gre


def resultados_dos_jogos():
    vitoria_do_inter = 0
    vitoria_do_gremio = 0
    empate = 0
    total_de_jogos = 0
    while True:
        placar_do_inter, placar_do_gremio = entrada()
        total_de_jogos += 1
        if placar_do_inter > placar_do_gremio:
            vitoria_do_inter += 1
        elif placar_do_inter < placar_do_gremio:
            vitoria_do_gremio += 1
        else:
            empate += 1
        continuar_confronto = novo_grenal()
        if continuar_confronto == 2:
            break
    print(f'{total_de_jogos} grenais')
    print(f'Inter:{vitoria_do_inter}')
    print(f'Gremio:{vitoria_do_gremio}')
    print(f'Empates:{empate}')
    if vitoria_do_inter > vitoria_do_gremio:
        print('Inter venceu mais')
    elif vitoria_do_inter < vitoria_do_gremio:
        print('Gremio venceu mais')
    else:
        print('Nao houve vencedo')


def novo_grenal():
    while True:
        nova_partida = int(input('Novo grenal (1-sim 2-nao)\n'))
        if nova_partida == 1 or nova_partida == 2:
            break
    return nova_partida


resultados_dos_jogos()
