def jogo_do_operador():
    while True:
        expressoes = list()
        resposta_dos_jogadores = list()
        jogadores_que_erraram = list()
        try:
            quantidade_de_expressoes = int(input())
            for expre in range(quantidade_de_expressoes):
                expressoes.append(list(map(str, input().split())))
            for resposta in range(quantidade_de_expressoes):
                resposta_dos_jogadores.append(list(map(str, input().split())))
            for i in resposta_dos_jogadores:
                nome_do_jogador = i[0]
                indice = int(i[1]) - 1
                expressao = i[2]
                operador_x = int(expressoes[indice][0])
                operador_y = int(expressoes[indice][1].replace('=', ' ').split()[0])
                operador_z = int(expressoes[indice][1].replace('=', ' ').split()[1])

                if expressao == '+':
                    if operador_x + operador_y != operador_z:
                        jogadores_que_erraram.append(nome_do_jogador)
                elif expressao == '-':
                    if operador_x - operador_y != operador_z:
                        jogadores_que_erraram.append(nome_do_jogador)
                elif expressao == '*':
                    if operador_x * operador_y != operador_z:
                        jogadores_que_erraram.append(nome_do_jogador)
            jogadores_que_erraram.sort()
            if jogadores_que_erraram:
                if len(jogadores_que_erraram) != quantidade_de_expressoes:
                    for jogador in jogadores_que_erraram:
                        if jogador == jogadores_que_erraram[len(jogadores_que_erraram)-1]:
                            print(jogador)
                        else:
                            print(jogador, end=' ')
                else:
                    print('None Shall Pass!')
            else:
                print('You Shall All Pass!')
        except EOFError:
            break
        except ValueError:
            break


jogo_do_operador()
