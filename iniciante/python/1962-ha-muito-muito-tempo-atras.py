def ha_muito_tempo_atras():
    n = int(input())
    for i in range(n):
        anos = int(input())
        if anos > 2014:
            print(f'{anos-2014} A.C.')
        else:
            print(f'{2015-anos} D.C.')


ha_muito_tempo_atras()
