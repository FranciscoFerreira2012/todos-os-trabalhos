from random import randint
import os

def Limpar():
    os.system("cls")
    
def Cabecalho(texto):
    Limpar()
    tamanho = len(texto) + 6
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)
    print()
    
def SubCabecalho(texto):
    print()
    print(f"### {texto} ###")
    print()

def Menu():
    Cabecalho("Jogo do Pedra Papel Tesoura")
    SubCabecalho("Menu")
    escolha = int(input(" 1 - Jogar contra PC \n 2 - Jogar contra Jogador \n 0 - Sair\n\n Escolha: "))
    
    return escolha

def Jogar():
    print("\n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n 0 - Sair\n")

def JogoPC():
    Limpar()
    SubCabecalho("Vez do Jogador 1")
    Jogar()
    jogadaUm = int(input("Escolha: "))
    input("\n Enter Para Continuar")
    if jogadaUm == 0:
        return
    Limpar()
    SubCabecalho("Vez do Jogador 2")
    print("O Computador escolheu a sua Jogada")
    jogadaDois = randint(1,3)
    input("\n Enter Para Continuar")
    LogicaJogo(jogadaUm, jogadaDois)
    
def JogoPlayer():
    Limpar()
    SubCabecalho("Vez do Jogador 1")
    Jogar()
    jogadaUm = int(input("Escolha: "))
    input("\n Enter Para Continuar")
    if jogadaUm == 0:
        return
    Limpar()
    SubCabecalho("Vez do Jogador 2")
    jogadaDois = int(input("Escolha: "))
    input("\n Enter Para Continuar")
    if jogadaDois == 0:
        return
    LogicaJogo(jogadaUm, jogadaDois)
    
def LogicaJogo(jogadaUm, jogadaDois):
    jogadas = ["Pedra", "Papel", "Tesoura"]
    
    if jogadaUm == 1:
        if jogadaDois == 1: 
            Limpar()
            SubCabecalho("Foi Empate!")
        if jogadaDois == 2:
            Limpar()
            SubCabecalho("O Jogador 2 Ganhou!")
        if jogadaDois == 3:
            Limpar()
            SubCabecalho("O Jogador 1 Ganhou!")
    if jogadaUm == 2:
        if jogadaDois == 1: 
            Limpar()
            SubCabecalho("O Jogador 1 Ganhou!")
        if jogadaDois == 2:
            Limpar()
            SubCabecalho("Foi Empate!")
        if jogadaDois == 3:
            Limpar()
            SubCabecalho("O Jogador 2 Ganhou!")
    if jogadaUm == 3:
        if jogadaDois == 1: 
            Limpar()
            SubCabecalho("O Jogador 2 Ganhou!")
        if jogadaDois == 2:
            Limpar()
            SubCabecalho("O Jogador 1 Ganhou!")
        if jogadaDois == 3:
            Limpar()
            SubCabecalho("Foi Empate!")
            
    print(f"\n O jogador 1 jogou {jogadas[jogadaUm - 1]} e o jogador 2 jogou {jogadas[jogadaDois - 1]}")
    input("\n Enter Para Continuar")
        
def Jogo():
    Cabecalho("Jogo do Pedra Papel Tesoura")
    input("\n\nEnter Para Inicar")
    while True:
        Cabecalho("Jogo do Pedra Papel Tesoura")
        escolha = Menu()
        Limpar()
        if escolha == 0:
            SubCabecalho("Sayonara".upper())
            break
        elif escolha == 1:
            JogoPC()
        elif escolha == 2:
            JogoPlayer()
        else:
            SubCabecalho("Escolha nao valida!")

Jogo()

