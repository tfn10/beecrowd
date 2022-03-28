def paridade():
    mensagem_s = input()
    quantidade_de_1 = mensagem_s.count('1')
    if quantidade_de_1 % 2 == 0:
        mensagem_s += '0'
    else:
        mensagem_s += '1'
    print(mensagem_s)


paridade()
