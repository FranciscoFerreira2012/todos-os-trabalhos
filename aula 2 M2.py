from tkinter import *

def Teste():
    labelTeste=Label(janela,text='Olá',font='Time 20 bold')
    labelTeste.place(width=100,height=50,x=200,y=200)
    
    buttonclick = Button(janela, text='Clique aqui', command=TesteDois, font='Time 20 bold')
    buttonclick.place(width=850, height= 60, x=100, y=300)
def TesteDois():
    labelTeste=Label(janela,text='Olá dois',font='Time 20 bold')
    labelTeste.place(width=150,height=50,x=600,y=200)   

janela = Tk()
janela.title("olá")
janela.geometry('1000x500+500+20')
janela.wm_resizable(width=True, height=True)


buttonclick = Button(janela, text='Clique aqui', command=Teste, font='Time 20 bold')
buttonclick.place(width=850, height= 60, x=100, y=50)

janela.mainloop()