def patinhos():
    while True:
        quantidade_total_de_patos = int(input())
        if quantidade_total_de_patos == -1:
            break
        elif quantidade_total_de_patos == 0:
            print(0)
        else:
            quantidade_patos_que_retornaram = quantidade_total_de_patos - 1
            print(quantidade_patos_que_retornaram)


patinhos()
