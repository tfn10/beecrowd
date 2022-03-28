def entrada():
    experimento = input().split(' ')
    quant = int(experimento[0])
    animal = experimento[1]
    return quant, animal


def experiencias(numero_de_teste):
    quantidade_de_cobaias = dict()
    for teste in range(numero_de_teste):
        quantidade, cobaia = entrada()
        if cobaia not in quantidade_de_cobaias:
            quantidade_de_cobaias[cobaia] = quantidade
        else:
            quantidade_de_cobaias[cobaia] += quantidade
    saida(quantidade_de_cobaias)


def saida(numero_de_cobaias):
    total_de_coelhos = numero_de_cobaias['C']
    total_de_ratos = numero_de_cobaias['R']
    total_de_sapos = numero_de_cobaias['S']
    total_de_cobais = total_de_coelhos + total_de_ratos + total_de_sapos
    percentual_de_coelhos = total_de_coelhos / total_de_cobais * 100
    percentual_de_ratos = total_de_ratos / total_de_cobais * 100
    percentual_de_sapos = total_de_sapos / total_de_cobais * 100
    return print(f'Total: {total_de_cobais} cobaias\n'
                 f'Total de coelhos: {total_de_coelhos}\n'
                 f'Total de ratos: {total_de_ratos}\n'
                 f'Total de sapos: {total_de_sapos}\n'
                 f'Percentual de coelhos: {percentual_de_coelhos:.2f} %\n'
                 f'Percentual de ratos: {percentual_de_ratos:.2f} %\n'
                 f'Percentual de sapos: {percentual_de_sapos:.2f} %')


numero_de_experimentos = int(input())
experiencias(numero_de_experimentos)
