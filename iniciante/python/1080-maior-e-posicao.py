def maior_posicao():
    posicao = maior = 0
    for i in range(1, 101):
        numero = int(input())
        if numero > maior:
            maior = numero
            posicao = i
    print(f'{maior}\n'
          f'{posicao}')


maior_posicao()
