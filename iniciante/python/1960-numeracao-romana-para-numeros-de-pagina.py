def numeracao_romanos():
    n = int(input())
    resto = n
    numeros_romanos = {1000: 'M',
                       900: 'CM',
                       500: 'D',
                       400: 'CD',
                       100: 'C',
                       90: 'XC',
                       50: 'L',
                       40: 'XL',
                       10: 'X',
                       9: 'IX',
                       5: 'V',
                       4: 'IV',
                       1: 'I'}
    for numeros_arabicos in numeros_romanos:
        divisores = resto // numeros_arabicos
        resto = resto % numeros_arabicos
        print(numeros_romanos[numeros_arabicos]*divisores, end='')
    print()


numeracao_romanos()
