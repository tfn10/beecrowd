def reservatorio_de_mel():
    while True:
        try:
            volume = float(input())
            diametro = float(input())
            area = ((100*3.14)*((100*diametro)/2)**2)/1000000
            altura = (volume*100)/(area*100)
            print(f'ALTURA = {altura:.2f}\n'
                  f'AREA = {area:.2f}')
        except ValueError:
            break
        except EOFError:
            break


reservatorio_de_mel()
