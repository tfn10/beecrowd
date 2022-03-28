def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        if i != (n-1):
            print(a, end=' ')
        else:
            print(a)
        a, b = b, a + b


numero = int(input())
fibonacci(numero)
