def soma_impares_consecutivos(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    soma_impares= 0
    for n in range(num1 + 1, num2):
        if n % 2 != 0:
            soma_impares += n
    return print(soma_impares)


numero1 = int(input())
numero2 = int(input())
soma_impares_consecutivos(numero1, numero2)
