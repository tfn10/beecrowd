def resposta_de_theon():
    n = int(input())
    numeros = list(map(int, input().split()))
    posicao = numeros.index(min(numeros)) + 1
    print(posicao)


resposta_de_theon()
