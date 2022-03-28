def voleibol():
    numero_de_jogadores = int(input())
    total_de_saques_tentados = 0
    total_de_saques_certos = 0
    total_de_bloqueios_tentatos = 0
    total_de_bloqueios_certos = 0
    total_de_ataques_tentados = 0
    total_de_ataques_certos = 0

    for jogador in range(numero_de_jogadores):
        nome_do_jogador = input()

        entrada_tentativas = list(map(int, input().split()))
        total_de_saques_tentados += entrada_tentativas[0]
        total_de_bloqueios_tentatos += entrada_tentativas[1]
        total_de_ataques_tentados += entrada_tentativas[2]

        entrada_sucesso = list(map(int, input().split()))
        total_de_saques_certos += entrada_sucesso[0]
        total_de_bloqueios_certos += entrada_sucesso[1]
        total_de_ataques_certos += entrada_sucesso[2]

    eficiencia_saque = float(total_de_saques_certos/total_de_saques_tentados*100)
    eficiencia_bloqueio = float(total_de_bloqueios_certos/total_de_bloqueios_tentatos*100)
    eficiencia_ataque = float(total_de_ataques_certos/total_de_ataques_tentados*100)

    print(f'Pontos de Saque: {eficiencia_saque:.2f} %.\n'
          f'Pontos de Bloqueio: {eficiencia_bloqueio:.2f} %.\n'
          f'Pontos de Ataque: {eficiencia_ataque:.2f} %.')


voleibol()
