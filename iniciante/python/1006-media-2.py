def media(a, b, c):
    """Calcula a média ponderada de três notas"""
    med = ((2 * a) + (3 * b) + (5 * c))/10
    return print(f'MEDIA = {med:.1f}')


def validacao_nota(nota):
    """Retorna uma nota entre 0 e 10"""
    if nota < 0 or nota > 10:
        while True:
            nota = entrada_nota()
            if 0 <= nota <= 10:
                break
    return nota


def entrada_nota():
    nota = float(input())
    nota_valida = validacao_nota(nota)
    return nota_valida


nota1 = entrada_nota()
nota2 = entrada_nota()
nota3 = entrada_nota()
media(nota1, nota2, nota3)
