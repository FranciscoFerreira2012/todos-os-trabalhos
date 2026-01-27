#Máquina do casino em que o utilizador mete dinheiro para apostar a cor que calhar 
#Se acertar a cor preta, que é a mais rara de calhar, ganha o valor de volta com mais 75% do valor original, se acertar em vermelho ou branco recebe o valor original e recebe 25% do valor mas se errar perde 50% do valor
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
    print(f"### {texto} ###")
    print()

def Menu():
    SubCabecalho("Menu")
    print("\n 1 - Escolher a cor \n 2 - Sair \n")
    escolha = int(input("\n Escolha: "))    
    return escolha


def MaquinaDoCasino():
    cores = ['Preto', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Preto', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho']
    Cabecalho("Roleta do casino")
    print("Insira o valor de dinheiro que você quer usar em euros.")
    dinheiro = int(input('Valor: '))
    numero = randint(0, len(cores) - 1)
    cor = cores[numero]
    Cabecalho("Vamos Jogar!")
    print()
    print(' 1-Preto\n 2-Vermelho\n 3-Branco')
    print()
    print("Qual é a cor que quer escolher (Vermelho, Preto ou Branco)?")
    escolha = input('Escolha: ')
    Limpar()
    if escolha.title() == cor and (escolha.title() == cores[1] or escolha.title() == cores[2]):        
        valorFinal = dinheiro*0.25
        print("Voce acertou!")
    elif escolha.title() == cor and escolha.title() == cores[0]:
        valorFinal = dinheiro*0.75
        print("Voce acertou!")
    elif escolha.title() != cor:
        valorFinal = dinheiro*0.50*(-1)
        print("Voce Errou!")
    dinheiro += valorFinal
    print(f'A Cor Secreta é {cores[numero]} e você escolheu a cor {escolha} e agora vai ter uma alteração de {valorFinal:.2f}€')
    print(f"O seu dinheiro atual é de {dinheiro}€")
    input("\n Enter Para Continuar")


def Jogo():
    Cabecalho("Roleta do casino")
    input("\n\nEnter Para Inicar")
    while True:
        Cabecalho("Roleta do casino")
        escolha = Menu()
        Limpar()
        if escolha == 2:
            SubCabecalho("Sayonara".upper())
            break
        elif escolha == 1:
            MaquinaDoCasino()
        else:
            SubCabecalho("Escolha nao valida!")

Jogo()






MaquinaDoCasino()
