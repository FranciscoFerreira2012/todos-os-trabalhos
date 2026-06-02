from tkinter import *
janela = Tk()
janela.title('Agenda')
janela.geometry('380x500+500+100')
janela.wm_resizable(width=False, height=False)






labelTitulo = Label(janela, text='Calculadora de IMC', font='Time 30', anchor='w')
labelTitulo.place(width=500, height=50, x=10, y=20)


labelPeso = Label(janela, text='Peso (Kg):', font='Time 10', anchor='w')
labelPeso.place(width=60, height=20, x=10, y=150)
inputPeso = Entry(janela, font='Time 10')
inputPeso.place(width=100, height=20, x=100, y=150)
janela.mainloop()