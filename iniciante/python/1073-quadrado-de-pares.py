def quadrado_de_pares(numero):
    for num in range(2, numero + 1, 2):
        print(f'{num}^2 = {num ** 2}')


n = int(input())
quadrado_de_pares(n)
