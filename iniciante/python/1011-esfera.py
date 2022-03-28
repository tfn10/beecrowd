def volume_esfera(raio):
    volume = (4/3) * 3.14159 * raio ** 3
    return print(f'VOLUME = {volume:.3f}')


r = int(input())
volume_esfera(r)
