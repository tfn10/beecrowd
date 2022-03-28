def media(nota1, nota2):
    med = (3.5 * nota1 + 7.5 * nota2)/11
    return print(f'MEDIA = {med:.5f}')


n1 = float(input())
n2 = float(input())
media(n1, n2)
