def entrada_notas():
    notas = input().split(' ')
    nota1 = float(notas[0])
    nota2 = float(notas[1])
    nota3 = float(notas[2])
    nota4 = float(notas[3])
    return nota1, nota2, nota3, nota4


def media(n1, n2, n3, n4):
    med = (2 * n1 + 3 * n2 + 4 * n3 + n4)/10
    print(f'Media: {med:.1f}')
    if med >= 7.0:
        print('Aluno aprovado.')
    elif med < 5.0:
        print('Aluno reprovado.')
    elif 5.0 <= med <= 6.9:
        print('Aluno em exame.')
        exame_final = float(input())
        print(f'Nota do exame: {exame_final:.1f}')
        nota_final = (exame_final + med)/2
        if nota_final >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado')
        print(f'Media final: {nota_final}')


exame1, exame2, exame3, exame4 = entrada_notas()
media(exame1, exame2, exame3, exame4)
