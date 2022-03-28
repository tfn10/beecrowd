def filme():
    valores = list(map(float, input().split()))
    a = valores[0]
    b = valores[1]
    porcentagem_aumento = ((b*100)*10000/(a*100))/100 - 100
    print(f'{porcentagem_aumento:.2f}%')


filme()
