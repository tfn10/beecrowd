def idades():
    soma = 0
    quantidade_de_idades = 0
    while True:
        idade = int(input())
        if idade < 0:
            break
        soma += idade
        quantidade_de_idades += 1
    media = soma / quantidade_de_idades
    print(f'{media:.2f}')


idades()
