
def conversor():
    if tipo_convertida == 'km':
        medida_nova = medida / 1000
        return medida_nova
    elif tipo_convertida == 'hm':
        medida_nova = medida / 100
        return medida_nova
    elif tipo_convertida == 'dam':
        medida_nova = medida / 10
        return medida_nova
    elif tipo_convertida == 'dm':
        medida_nova = medida * 10
        return medida_nova
    elif tipo_convertida == 'cm':
        medida_nova = medida * 100
        return medida_nova
    elif tipo_convertida == 'mm':
        medida_nova = medida * 1000
        return medida_nova

while True:
    medida = float(input('Digite uma medida em metros que deseja converter: '))
    tipo_convertida = input('Digite para qual tipo deseja converter: ')

    print(f'A sua medida corresponde a {conversor()} {tipo_convertida}.')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break