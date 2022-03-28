def tipo_de_combustivel():
    alcool = 0
    gasolina = 0
    diesel = 0
    while True:
        codigo_do_combustivel = int(input())
        if codigo_do_combustivel == 1:
            alcool += 1
        elif codigo_do_combustivel == 2:
            gasolina += 1
        elif codigo_do_combustivel == 3:
            diesel += 1
        elif codigo_do_combustivel == 4:
            break
    print(f'MUITO OBRIGADO\n'
          f'Alcool: {alcool}\n'
          f'Gasolina: {gasolina}\n'
          f'Diesel: {diesel}')


tipo_de_combustivel()
