def sequencia_de_sequencia():
    caso = 1
    while True:
        try:
            numero = int(input())
            if numero == 0:
                print(f'Caso {caso}: 1 numero\n'
                      f'0\n')
            else:
                tamanho_sequencia, seq = sequencia(numero)
                print(f'Caso {caso}: {tamanho_sequencia} numeros\n'
                      f'{seq}\n')
            caso += 1
            pass
        except EOFError:
            break
        except ValueError:
            break


def sequencia(n):
    lista_da_sequencia = list()
    for count in range(n+1):
        i = 0
        if count == 0:
            lista_da_sequencia.append(0)
        else:
            while i < count:
                lista_da_sequencia.append(count)
                i += 1
    tamanho_da_sequencia = len(lista_da_sequencia)
    sequencia_imprimida = ' '.join(str(_) for _ in lista_da_sequencia)
    return tamanho_da_sequencia, sequencia_imprimida


sequencia_de_sequencia()
