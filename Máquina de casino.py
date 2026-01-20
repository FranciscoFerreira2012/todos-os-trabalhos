#Máquina do casino em que o utilizador mete dinheiro para apostar a cor que calhar 
#Se acertar a cor preta, que é a mais rara de calhar, ganha o valor de volta com mais 75% do valor original, se acertar em vermelho ou branco recebe o valor original e recebe 25% do valor mas se errar perde 50% do valor
from random import randint
def MaquinaDoCasino():
    cores = ['Preto', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Preto', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho']
    dinheiro = int(input('Insira o valor de dinheiro que você quer usar em euros '))
    numero = 0
    cor = cores[numero]
    print()
    print('1-Preto\n2-Vermelho\n3-Branco')
    print(cor)
    escolha = input('Qual é a cor que quer escolher (Vermelho, Preto ou Branco)? ')
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





MaquinaDoCasino()