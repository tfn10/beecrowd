def fibonacci_em_vetor():
    numero_de_teste = int(input())
    for i in range(numero_de_teste):
        n = int(input())
        sequencia_fib = fibonacci()
        print(f'Fib({n}) = {sequencia_fib[n]}')


def fibonacci():
    sequencia_fibonacci = list()
    a = 0
    b = 1
    for j in range(61):
        sequencia_fibonacci.append(a)
        a, b = b, a+b
    return sequencia_fibonacci


fibonacci_em_vetor()
