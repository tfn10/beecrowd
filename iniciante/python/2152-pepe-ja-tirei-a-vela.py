def ja_tirei_a_vela():
    n = int(input())
    for numero in range(n):
        entrada = list(map(int, input().split()))
        hora = entrada[0]
        minuto = entrada[1]
        fechou_ou_abriu = entrada[2]
        print(f'{str(hora).zfill(2)}:{str(minuto).zfill(2)} - ', end='')
        if fechou_ou_abriu == 0:
            print('A porta fechou!')
        else:
            print('A porta abriu!')


ja_tirei_a_vela()
