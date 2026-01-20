import random

numeroSorteados = []
somaPares = 0
numerosPares = 0
soma = 0

def GeradorDeNumerosAleatorios():

    for i in range(1,11):
        numero = random.randint(1,100)
        numeroSorteados.append(numero)

    print(f'Os 10 valores sorteados foram: {numeroSorteados}')
    print()

def SomaDosNumerosPares():
    global somaPares
    numerosPares = []

    for numero in numeroSorteados:
        if numero % 2 == 0:
            numerosPares.append(numero)
            somaPares += numero
    
    print(f'Os numeros pares são: {numerosPares}')
    print()
    print(f'A soma dos valores pares contidos na lista {numeroSorteados} é {somaPares}')
    print()

def SomaTodosNumeros():

    global soma

    for numero in numeroSorteados:
        soma += numero
    
    soma += somaPares


    print(f'A soma dos valores pares contidos nas listas é {soma}')


GeradorDeNumerosAleatorios()
SomaDosNumerosPares()
SomaTodosNumeros()
