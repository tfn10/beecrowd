def fibonacci():
    n = int(input())
    valor_de_fibonacci = float((((1 + (5**(1/2)))/2) ** n - ((1 - (5**(1/2)))/2) ** n)/(5 ** (1/2)))
    print(f'{valor_de_fibonacci:.1f}')


fibonacci()
