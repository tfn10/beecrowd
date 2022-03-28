def andando_no_tempo():
    creditos = list(map(int, input().split()))
    credito_a = creditos[0]
    credito_b = creditos[1]
    credito_c = creditos[2]
    if credito_a == credito_b\
            or credito_b == credito_c\
            or credito_a == credito_c:
        print('S')
    elif credito_a + credito_b == credito_c\
            or credito_a + credito_c == credito_b\
            or credito_b + credito_c == credito_a:
        print('S')
    else:
        print('N')


andando_no_tempo()
