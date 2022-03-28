def galopeira():
    n = int(input())
    for numero in range(n):
        palavra = input()
        tamanho_da_palavra = len(palavra)
        tempo_gasto = 0.01 * tamanho_da_palavra
        print(f'{tempo_gasto:.2f}')


galopeira()
