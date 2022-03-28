def abas_de_pericles():
    entrada = list(map(int, input().split()))
    numero_de_abas = entrada[0]
    numero_de_acoes = entrada[1]
    for i in range(numero_de_acoes):
        acao = input()
        if acao == 'fechou':
            numero_de_abas += 1
        elif acao == 'clicou':
            numero_de_abas -= 1
    print(numero_de_abas)


abas_de_pericles()
