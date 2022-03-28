def pum():
    j = 1
    quantidade_de_linhas = int(input())
    for i in range(quantidade_de_linhas):
        t = 0
        while t < 3:
            print(j, end=' ')
            t += 1
            j += 1
        j += 1
        print('PUM')


pum()
