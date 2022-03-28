def validacao_de_nota():
    notas_validas = soma = 0
    while True:
        if notas_validas == 2:
            break
        nota = float(input())
        if 0 <= nota <= 10:
            soma += nota
            notas_validas += 1
        else:
            print('nota invalida')
    media = soma / 2
    print(f'media = {media:.2f}')


validacao_de_nota()
