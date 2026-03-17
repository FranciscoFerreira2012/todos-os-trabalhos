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
    Cabecalho("Criador de ficheiros")
    SubCabecalho("Menu")
    escolha = int(input(" 1 - Criar Ficheiro \n 2 - Conteudo do ficheiro \n 3 - Ler Ficheiro\n 4 - Encontrar Palavra\n 0- Sair \n\nEscolha: "))
    
    return escolha

def Jogo():
    Cabecalho("Criador de ficheiros")
    input("\n\nEnter Para Inicar")
    while True:
        Cabecalho("Criador de ficheiros")
        escolha = Menu()
        Limpar()
        if escolha == 0:
            SubCabecalho("Sayonara".upper())
            break
        elif escolha == 1:
            NomeFicheiro()
        elif escolha == 2:
            ConteudoFicheiro()
        elif escolha == 3:
            LerFicheiro()
        elif escolha == 4:
            EncontrarPalavra()
        else:
            SubCabecalho("Escolha nao valida!")


def UtilizadorNomeficheiro():
    global nomeFicheiro
    nomeFicheiro = input('Qual é o nome do ficheiro?\n')

def NomeFicheiro():
    UtilizadorNomeficheiro()
    open(f'{nomeFicheiro}.txt', 'w', encoding='utf-8')

    print(f'o aquivo "{nomeFicheiro}.txt" foi criado com sucesso!')

def UtilizadorConteudoFicheiro():
    global conteudoFicheiro
    conteudoFicheiro = input('Qual o conteudo do ficheiro? ')

def ConteudoFicheiro():
    UtilizadorConteudoFicheiro()
    with open(f'{nomeFicheiro}.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(conteudoFicheiro)

    print(f'O conteudo ({conteudoFicheiro}) foi adicionado ao ficheiro "{nomeFicheiro}.txt" com sucesso!')

def UtilizadorLerFicheiro():
    validacao = input('\nQuer ler o ficheiro? Sim(S) Não(N): ')

    if validacao.upper() == 'S':
        return True
    
    return False

def LerFicheiro():
    validacao = UtilizadorLerFicheiro()
    if validacao:
        with open(f'{nomeFicheiro}.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo)

def UtilizadorEncontrarPalavra():
    global palavra
    palavra = input('Qual é a palavra que deseja encontrar? ')

def EncontrarPalavra():
    UtilizadorEncontrarPalavra()
    with open(f'{nomeFicheiro}.txt', 'r', encoding='utf-8') as ficheiro:
        for linha in ficheiro:
            if (palavra) in linha:
                print(linha.rstrip())

Jogo()