def animal():
    coluna_vertebral = input()
    if coluna_vertebral == 'vertebrado':
        vertebrado = input()
        if vertebrado == 'ave':
            ave = input()
            if ave == 'carnivoro':
                print('aguia')
            elif ave == 'onivoro':
                print('pomba')
        elif vertebrado == 'mamifero':
            mamifero = input()
            if mamifero == 'onivoro':
                print('homem')
            elif mamifero == 'herbivoro':
                print('vaca')
    elif coluna_vertebral == 'invertebrado':
        invertebrado = input()
        if invertebrado == 'inseto':
            inseto = input()
            if inseto == 'hematofago':
                print('pulga')
            elif inseto == 'herbivoro':
                print('lagarta')
        elif invertebrado == 'anelideo':
            anelideo = input()
            if anelideo == 'hematofago':
                print('sanguessuga')
            elif anelideo == 'onivoro':
                print('minhoca')


animal()
