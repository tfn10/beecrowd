def saltos_ornamentais():
    numero_de_competidores = int(input())
    for competidor in range(numero_de_competidores):
        nome_do_competidor = input()
        grau_de_dificuldade_do_salto = float(input())
        notas_recebidas = list(map(float, input().split()))
        resultado_parcial = sum(notas_recebidas) - min(notas_recebidas) - max(notas_recebidas)
        resultado_final = resultado_parcial * grau_de_dificuldade_do_salto
        print(f'{nome_do_competidor} {resultado_final:.2f}')


saltos_ornamentais()
