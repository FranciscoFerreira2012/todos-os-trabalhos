from random import randint
lutadorB = 10000
lutadorA = 10000

def VidaDoLutadorB(soco):
    global lutadorB
    lutadorB = lutadorB - soco
    print(f"O lutador A deu um murro de força {soco} e a vida do lutador B foi para {lutadorB}.")

def VidaDoLutadorA(soco):
    global lutadorA
    lutadorA = lutadorA - soco
    print(f'O lutador B deu um murro de força {soco} e a vida do lutador A foi para {lutadorA}.')


def LutaDeBox():
    global lutadorA
    global lutadorB
    while True:

        if lutadorA and lutadorB > 0:
            soco = randint(0, 1000)
            
            VidaDoLutadorB(soco)
        if lutadorB > 0:
            soco = randint(0, 1000)
            
            VidaDoLutadorA(soco)

        if lutadorB <= 0:
            print("O lutador A ganhou a luta!!!!!!")
            break
        elif lutadorA <= 0:
            print("O lutador B ganhou a luta!!!!!!")
            break

LutaDeBox()

