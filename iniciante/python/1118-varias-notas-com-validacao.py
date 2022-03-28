def validacao_de_nota():
    while True:
        soma_notas, valida_nota = calculo_das_somas()
        media = soma_notas / valida_nota
        print(f'media = {media:.2f}')
        novo_calculo = calculo_novo()
        if novo_calculo == 2:
            break


def calculo_das_somas():
    soma_das_notas = notas_validas = 0
    while True:
        if notas_validas == 2:
            break
        nota = float(input())
        if 0.0 <= nota <= 10.0:
            soma_das_notas += nota
            notas_validas += 1
        else:
            print('nota invalida')
    return soma_das_notas, notas_validas


def calculo_novo():
    while True:
        continuar = int(input('novo calculo (1-sim 2-nao)\n'))
        if continuar == 1 or continuar == 2:
            break
    return continuar


validacao_de_nota()
