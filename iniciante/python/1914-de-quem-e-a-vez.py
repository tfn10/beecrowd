def de_quem_e_a_vez():
    numero_de_testes = int(input())
    for i in range(numero_de_testes):
        jogada = input().split()
        jogadores_e_escolha = {jogada[1]: jogada[0], jogada[3]: jogada[2]}
        numeros = list(map(int, input().split()))
        soma_dos_numeros = sum(numeros)
        if soma_dos_numeros % 2 == 0:
            print(jogadores_e_escolha['PAR'])
        else:
            print(jogadores_e_escolha['IMPAR'])


de_quem_e_a_vez()
