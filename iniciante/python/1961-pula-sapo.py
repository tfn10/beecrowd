def pula_sapo():
    valores_linha1 = list(map(int, input().split()))
    altura_do_sapo = valores_linha1[0]
    numero_de_canos = valores_linha1[1]
    alturas_dos_canos = list(map(int, input().split()))
    a = alturas_dos_canos[0]
    b = alturas_dos_canos[1]
    vencedor = 'YOU WIN'
    if numero_de_canos > 2:
        for altura in alturas_dos_canos[2:]:
            diferenca = abs(a-b)
            if diferenca > altura_do_sapo:
                vencedor = 'GAME OVER'
                break
            a = b
            b = altura
    else:
        diferenca = abs(a-b)
        if diferenca > altura_do_sapo:
            vencedor = 'GAME OVER'
    print(vencedor)


pula_sapo()
