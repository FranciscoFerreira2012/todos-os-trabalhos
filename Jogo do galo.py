import os

def Limpar():
    os.system('cls')

def Cabecalho(texto):
    Limpar()
    cumprimento = len(texto) + 6
    print()
    print('='*cumprimento)
    print(f'|| {texto} ||')
    print('='*cumprimento)
    print()

def SubCabecalho(texto):
    Limpar()
    print()
    print(f'### {texto} ###')
    print()

def Menu():
    SubCabecalho('Menu')
    escolha = int(print('0 - Sair \n 1 - Jogar contra PC \n 2 - Jogar contra jogaror\n'))
    return escolha

def JogoPC():

def JogoPlayer():

    jogadaUm = input ('Jogador 1:')
    jogadaDois = input ('Jogador 2:')
    LogicaJogo()

def LogicaJogo():
    
    jogadorUm = []
    
    jogadorDois = []

    while True:
        print('  {A1}  |  {A2}  |  {A3}  ')
        print('  |  |  |  ')
        print('='*11)
        print('  |  |  |  ')
        print('  {B1}  |  {B2}  |  {B3}  ')
        print('  |  |  |  ')
        print('='*11)
        print('  |  |  |  ')
        print('  {C1}  |  {C2}  |  {C3}  ')
        print('  |  |  |  ')
def Jogo():
    Cabecalho('Jogo do Galo')
    input('\n\nEnter para iniciar')
    while True:
        escolha = Menu()
        if escolha == 0:
            Limpar()
            break
        elif escolha == 1:
            JogoPC()
        elif escolha == 2:
            JogoPlayer()
        else:
            SubCabecalho('Escolha nao valida!')


Jogo()
Menu()