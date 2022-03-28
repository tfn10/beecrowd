def decifrando_a_carta_criptografada():
    while True:
        try:
            entrada = list(map(int, input().split()))
            tamanho_da_cifra = entrada[0]
            quantidade_de_cifras = entrada[1]
            caracteres_1 = input()
            caracteres_2 = input()
            carta_criptografada(quantidade_de_cifras, caracteres_1, caracteres_2)
        except ValueError:
            break
        except EOFError:
            break
        except IndexError:
            break


def carta_criptografada(quatidade_cifras, caracteres1, caracteres2):
    for i in range(quatidade_cifras):
        frase = input()
        nova_frase = str()
        for letra in frase:
            if letra != ' ':
                if letra.upper() in caracteres1.upper():
                    if letra.isupper():
                        posicao_da_letra = caracteres1.upper().find(letra.upper())
                        nova_frase += caracteres2[posicao_da_letra].upper()
                    else:
                        posicao_da_letra = caracteres1.upper().find(letra.upper())
                        nova_frase += caracteres2[posicao_da_letra].lower()
                elif letra.upper() in caracteres2.upper():
                    if letra.isupper():
                        posicao_da_letra = caracteres2.upper().find(letra.upper())
                        nova_frase += caracteres1[posicao_da_letra].upper()
                    else:
                        posicao_da_letra = caracteres2.upper().find(letra.upper())
                        nova_frase += caracteres1[posicao_da_letra].lower()
                else:
                    nova_frase += letra
            else:
                nova_frase += ' '
        print(nova_frase)
    print()


decifrando_a_carta_criptografada()
