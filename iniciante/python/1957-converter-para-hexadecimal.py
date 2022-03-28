def converter_para_hexadecimal():
    numero = int(input())
    convertido_para_hex = hex(numero)
    print(convertido_para_hex[2:].upper())


converter_para_hexadecimal()
