def Acharletra():
    frase = input('Digite a sua frase:')
    numeroDeLetras = input('Qual é a letra que deseja contar?')
    if numeroDeLetras in frase:
        print(f'Existe letra {numeroDeLetras}')
    else:
        print(f'Não existe letra {numeroDeLetras}')

Acharletra()