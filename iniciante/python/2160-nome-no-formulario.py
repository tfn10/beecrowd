def nome_no_formulario():
    nome = input()
    tamanho_de_caracteres = len(nome)
    if tamanho_de_caracteres > 80:
        print('NO')
    else:
        print('YES')


nome_no_formulario()
