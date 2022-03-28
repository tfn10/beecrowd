def sequencia():
    i = 1
    while True:
        j = 7
        for t in range(3):
            print(f'I={i} J={j}')
            j -= 1
        if i >= 9:
            break
        i += 2


sequencia()
