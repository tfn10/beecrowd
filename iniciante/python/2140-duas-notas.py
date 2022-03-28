def duas_notas():
    notas_disponiveis = [2, 5, 10, 20, 50, 100]
    while True:
        entrada = list(map(int, input().split()))
        compra_pelo_cliente = entrada[0]
        valor_pago = entrada[1]
        devolver_troco_exato = False
        if compra_pelo_cliente == valor_pago == 0:
            break
        troco = valor_pago - compra_pelo_cliente
        for i in range(len(notas_disponiveis)):
            for j in range(1, len(notas_disponiveis)):
                if troco / (notas_disponiveis[i]+notas_disponiveis[j]) == 1:
                    devolver_troco_exato = True
                    break
            if devolver_troco_exato:
                break
        if devolver_troco_exato:
            print('possible')
        else:
            print('impossible')


duas_notas()
