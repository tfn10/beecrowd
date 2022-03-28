def senha():
    while True:
        try:
            n = int(input())
            print(n-1)
        except ValueError:
            break
        except EOFError:
            break


senha()
