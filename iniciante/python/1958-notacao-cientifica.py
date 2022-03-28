def notacao_cientifica():
    n = float(input())
    if n == 0 and str(n)[0] != '-':
        print(f'+{n:.4E}')
    elif n == 0 and str(n)[0] == '-':
        print(f'{n:.4E}')
    elif n > 0:
        print(f'+{n:.4E}')
    else:
        print(f'{n:.4E}')


notacao_cientifica()
