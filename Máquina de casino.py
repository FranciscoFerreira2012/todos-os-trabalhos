#Máquina do casino em que o utilizador mete dinheiro para apostar a cor que calhar 
#Se acertar a cor preta, que é a mais rara de calhar, ganha o valor de volta com mais 75% do valor original, se acertar em vermelho ou branco recebe o valor original e recebe 25% do valor mas se errar perde 50% do valor
from random import randint
def MaquinaDoCasino():
    cores = ['Preto', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho', 'Branco', 'Vermelho']
    dinheiro = int(input('Insira o valor de dinheiro que você quer usar em euros '))
    numero = randint(0, len(cores))
    cor = cores[numero]
    print()
    print('1-Preto\n2-Vermelho\n3-Branco')
    print()
    escolha = input('Qual é a cor que quer escolher(1-3)? ')
    if escolha == numero:
        valorFinal = dinheiro+(dinheiro*0.25)
        print(f'Você acertou a cor e ganhou {valorFinal}€')
    elif escolha == numero:
        valorFinal = dinheiro+(dinheiro*0.25)
        print(f'Você acertou a cor e ganhou {valorFinal}€')
    elif escolha == numero == cores[0]:
        valorFinal = dinheiro+(dinheiro*0.75)
        print(f'Você acertou a cor preta e ganhou {valorFinal}€')   
    else:
        valorFinal = dinheiro*0.50
        print(f'Você errou, a cor era {cores[numero]} e perdeu {valorFinal}€')



MaquinaDoCasino()