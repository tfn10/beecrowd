def identificando_cha():
    tipo_de_cha = int(input())
    resposta_dada = list(map(int, input().split()))
    concorretes_que_acertaram = 0
    for cha in resposta_dada:
        if cha == tipo_de_cha:
            concorretes_que_acertaram += 1
    print(concorretes_que_acertaram)


identificando_cha()
