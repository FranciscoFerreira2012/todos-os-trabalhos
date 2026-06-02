import os

def limpar():
    os.system('cls')

def Cabecalho(texto):
    limpar()
    cumprimento = len(texto) + 6
    print()
    print("="*cumprimento)
    print(f"|| {texto} ||")
    print("="*cumprimento)
    print()
    
def SubCabecalho(texto):
    print()
    print(f"### {texto} ###")
    print()

def Cadastro():
    nome = input('Entre com o nome: ')
    idade = int(input('Entre com a idade: '))
    with open('Lista_Idades.txt','a', encoding="utf-8") as file:
        file.write(f'{nome}\n')
        file.write(f'{str(idade)}\n')

def EncontrarNome():
    nome = input("Qual nome deseja procurar?: ")
    with open("Lista_Idades.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.readlines()
    encontrado = False
    
    for linha in range(len(conteudo)):
        if nome.lower() in conteudo[linha].lower():
            print(f"\n\n Nome: {conteudo[linha].strip()}")

            if linha + 1 < len(conteudo):
                print(f" Idade: {conteudo[linha + 1].strip()}")
            encontrado = True
            print("-" * 20)
            
    if not encontrado:
        print("Nome não encontrado!")
            
    input("\n\n Enter Para Continuar!")

def Menu():
    Cabecalho("Cadastro")
    SubCabecalho("Menu")
    escolha = int(input(" 1 - Cadastrar \n 2 - Encontrar Nome \n 0 - Sair \n\n Escolha: "))
    
    return escolha

def Cadastrar():
    Cabecalho("Cadastro")
    input("\n\nEnter Para Iniciar")
    while True:
        limpar()
        escolha = Menu()
        limpar()
        if escolha == 0:
            Cabecalho("# Sayonara #".upper())
            break
        elif escolha == 1:
            Cadastro()
        elif escolha == 2:
            EncontrarNome()
        else:
            SubCabecalho("Escolha não válida!")
            input("\n\n Enter Para Continuar!")
            
Cadastrar()