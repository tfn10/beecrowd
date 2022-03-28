def tomadas():
    reguas = list(map(int, input().split()))
    t1 = reguas[0]
    t2 = reguas[1]
    t3 = reguas[2]
    t4 = reguas[3]
    numeros_de_aparelhos = t1 + t2 + t3 - 3 + t4
    print(numeros_de_aparelhos)


tomadas()
