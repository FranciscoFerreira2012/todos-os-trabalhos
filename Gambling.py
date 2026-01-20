from random import randint

def GirarOsDados ():
        
    dadoUm = 0
    dadoDois = 0
    contador = 0
    
    while True:
        contador +=1
        dadoUm = randint (1,6)
        dadoDois = randint (1,6)
        
        if (dadoUm == 6) and (dadoDois == 6):
            print(f"São necessários {contador} vezes para aparecer dois dados iguais a 6")
            break
        
GirarOsDados()