def bazinga():
    numeros_de_testes = int(input())
    for i in range(1, numeros_de_testes + 1):
        disputa = list(map(str, input().split()))
        sheldon = disputa[0]
        raj = disputa[1]
        if sheldon == 'tesoura':
            if raj == 'tesoura':
                print(f'Caso #{i}: De novo!')
            elif raj == 'papel':
                print(f'Caso #{i}: Bazinga!')
            elif raj == 'pedra':
                print(f'Caso #{i}: Raj trapaceou!')
            elif raj == 'largarto':
                print(f'Caso #{i}: Bazinga!')
            elif raj == 'Spock':
                print(f'Caso #{i}: Raj trapaceou!')
        elif sheldon == 'papel':
            if sheldon == 'tesoura':
                if raj == 'tesoura':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'papel':
                    print(f'Caso #{i}: De novo!')
                elif raj == 'pedra':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'largarto':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'Spock':
                    print(f'Caso #{i}: Bazinga!')
        elif sheldon == 'pedra':
            if sheldon == 'tesoura':
                if raj == 'tesoura':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'papel':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'pedra':
                    print(f'Caso #{i}: De novo!')
                elif raj == 'largarto':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'Spock':
                    print(f'Caso #{i}: Raj trapaceou!')
        elif sheldon == 'lagarto':
            if sheldon == 'tesoura':
                if raj == 'tesoura':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'papel':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'pedra':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'largarto':
                    print(f'Caso #{i}: De novo!')
                elif raj == 'Spock':
                    print(f'Caso #{i}: Bazinga!')
        elif sheldon == 'Spock':
            if sheldon == 'tesoura':
                if raj == 'tesoura':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'papel':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'pedra':
                    print(f'Caso #{i}: Bazinga!')
                elif raj == 'largarto':
                    print(f'Caso #{i}: Raj trapaceou!')
                elif raj == 'Spock':
                    print(f'Caso #{i}: De novo!')


bazinga()
