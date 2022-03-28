def sequencia():
    i = 0
    j = 1
    while i <= 2:
        for aux in range(3):
            if int(i) == i:
                print(f'I={int(i)} J={int(j)}')
            else:
                print(f'I={i:.1f} J={j:.1f}')
            j += 1
        j = round(j - 3 + 0.2, 1)
        i = round(i + 0.2, 1)


sequencia()
