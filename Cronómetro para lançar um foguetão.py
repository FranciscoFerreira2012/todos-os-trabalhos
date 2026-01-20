from time import sleep

def Contagem(contador):
    print(contador)
    sleep(1)

def Lançamento():
    contador = int(input('Qual é o número inicial da contagem'))
    while True:
        if contador == 0:
            print('A lançar o foguete.')
            break
        else:
            Contagem(contador)
            contador -= 1

   # for i in range(contador):
   #     Contagem(contador)
   #     contador -= 1
   #     if contador == 0:
   #         print('A lançar um foguete.')
   #         break

#pode-se usar ambas as maneiras, ou a maneira a verde ou a de cima.

Lançamento()