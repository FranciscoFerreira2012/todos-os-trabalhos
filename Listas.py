def conversãoDeTemperatura(temperatura):
    return((temperatura - 32) * (5/9))

def temperatura():
    valorDeTemperatura = float(input('Escree a temperatura'))

    temperatura = conversãoDeTemperatura(valorDeTemperatura)

    print(f'Temperatura = {temperatura:.2f}ºC')