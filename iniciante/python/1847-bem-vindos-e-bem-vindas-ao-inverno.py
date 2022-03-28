def inverno():
    dias = list(map(int, input().split()))
    dia1 = dias[0]
    dia2 = dias[1]
    dia3 = dias[2]
    # 1 - ok
    if dia1 > dia2 and (dia2 < dia3 or dia2 == dia3):
        print(':)')
    # 2 - ok
    elif dia1 < dia2 and (dia2 > dia3 or dia2 == dia3):
        print(':(')
    # 3 - ok
    elif dia1 < dia2 < dia3 and (dia3-dia2) < (dia2-dia1):
        print(':(')
    # 4 - ok
    elif dia1 < dia2 < dia3 and (dia3-dia2) >= (dia2-dia1):
        print(':)')
    # 5 - ok
    elif dia1 > dia2 > dia3 and (dia1-dia2) > (dia2-dia3):
        print(':)')
    # 6 - ok
    elif dia1 > dia2 > dia3 and (dia2-dia3) >= (dia2-dia1):
        print(':(')
    # 7 - ok
    elif dia1 == dia2:
        if dia2 < dia3:
            print(':)')
        else:
            print(':(')


inverno()
