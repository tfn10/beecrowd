def sequencia():
    i = 1
    j = 7
    while True:
        for t in range(3):
            print(f'I={i} J={j}')
            j -= 1
        j += 5
        if i >= 9:
            break
        i += 2


sequencia()
