def sequencia_logica():
    n = int(input())
    for i in range(1, n+1):
        quadrado = i ** 2
        cubo = i ** 3
        print(f'{i} {quadrado} {cubo}')
        print(f'{i} {quadrado+1} {cubo+1}')


sequencia_logica()
