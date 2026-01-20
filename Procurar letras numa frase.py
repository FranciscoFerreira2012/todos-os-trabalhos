def Acharletra():
    frase = input('Digite a sua frase:')
    numeroDeLetras = input('Qual é a letra que procuras?')
    if numeroDeLetras in frase:
        print(f'Existe letra {numeroDeLetras}')
    else:
        print(f'Não existe letra {numeroDeLetras}')

Acharletra()