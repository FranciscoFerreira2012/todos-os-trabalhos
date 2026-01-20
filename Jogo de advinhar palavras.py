from random import randint

def PensamentoComputaconal():
    
    numeroSecreto = randint (0,100)
        
    while True:

        escolha = int(input('Esolha um número de 0 a 100: '))
        if escolha == numeroSecreto:
            print('Parabéns!!!!!!!!!! Você acertou!!!!!!!!')
            break
        elif escolha > numeroSecreto:
            print('Você errou!!! O número certo era maior do que a sua escolha.')
        elif escolha < numeroSecreto:
            print('Você errou!!! O número certo era menor do que a sua escolha.')
        

PensamentoComputaconal()