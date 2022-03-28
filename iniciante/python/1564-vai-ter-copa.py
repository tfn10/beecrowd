def vai_ter_copa():
    while True:
        try:
            n = int(input())
            if 0 <= n <= 100:
                if n == 0:
                    print('vai ter copa!')
                else:
                    print('vai ter duas!')
        except EOFError:
            break
        except ValueError:
            break


vai_ter_copa()
