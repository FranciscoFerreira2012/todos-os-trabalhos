from tkinter import *

blue = '#143ed9'
red = '#db1e0d'
green = '#0ceb22'
yellow = '#f1f507'
white = '#ffffff'
black = '#000000'

def Blue():
    janela.configure(background=blue)
    labelColor.configure(text='Blue', bg=blue)

def Red():
    janela.configure(background=red)
    labelColor.configure(text='Red', bg=red)

def Yellow():
    janela.configure(background=yellow)
    labelColor.configure(text='Yellow', bg=yellow)

def Green():
    janela.configure(background=green)
    labelColor.configure(text='Green', bg=green)

janela = Tk()
janela.title("color changer")
janela.geometry('500x500+500+20')
janela.wm_resizable(width=True, height=True)
janela.configure(background=white)

buttonBlue = Button(janela, text='Blue', command=Blue, font='Arial 14 bold', bg=blue)
buttonBlue.place(width=200, height= 160, x=40, y=40)

buttonRed = Button(janela, text='Red', command=Red, font='Arial 14 bold', bg=red)
buttonRed.place(width=200, height= 160, x=260, y=40)

buttonYellow = Button(janela, text='Yellow', command=Yellow, font='Arial 14 bold', bg=yellow)
buttonYellow.place(width=200, height= 160, x=40, y=230)

buttonGreen = Button(janela, text='Green', command=Green, font='Arial 14 bold', bg=green)
buttonGreen.place(width=200, height= 160, x=260, y=230)

labelColor = Label(janela, text='Colour', font='Time 20 bold', bg=white)
labelColor.place(width=120, height=60, x=190 ,y=400)

janela.mainloop()