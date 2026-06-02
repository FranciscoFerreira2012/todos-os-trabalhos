from tkinter import *
from tkinter import messagebox

blue = '#143ed9'
red = '#db1e0d'
green = '#0ceb22'
yellow = '#f1f507'
white = '#ffffff'
black = '#000000'

janela = Tk()
janela.title('Agenda')
janela.geometry('380x500+500+100')
janela.wm_resizable(width=False, height=False)

labelAgenda = Label(janela, text='Sharkcoders Python', font='Time 20 bold', bg=yellow, fg=red, anchor='w', padx=10)
labelAgenda.place(width=380, height=50, x=0, y=0)

labelNome = Label(janela, text='Nome', font='Time 10', anchor='w')
labelNome.place(width=60, height=20, x=10, y=70)
inputNome = Entry(janela, font='Time 10')
inputNome.place(width=250, height=20, x=100, y=70)

labelTelemovel = Label(janela, text='Telemóvel', font='Time 10', anchor='w')
labelTelemovel.place(width=60, height=20, x=10, y=170)
inputTelemovel = Entry(janela, font='Time 10')
inputTelemovel.place(width=250, height=20, x=100, y=110)

labelEndereco = Label(janela, text='Endereço', font='Time 10', anchor='w')
labelEndereco.place(width=60, height=20, x=10, y=170)
inputEndereco = Entry(janela, font='Time 10')
inputEndereco.place(width=250, height=20, x=100, y=170)

labelDistrito = Label(janela, text='Distrito', font='Time 10', anchor='w')
labelDistrito.place(width=60, height=20, x=10, y=210)
inputDistrito = Entry(janela, font='Time 10')
inputDistrito.place(width=80, height=20, x=100, y=210)

labelPais = Label(janela, text='País', font='Time 10', anchor='w')
labelPais.place(width=60, height=20, x=210, y=210)
inputPais = Entry(janela, font='Time 10')
inputPais.place(width=250, height=20, x=100, y=270)

labelEmail = Label(janela, text='Email', font='Time 10', anchor='w')
labelEmail.place(width=60, height=20, x=10, y=270)
inputEmail = Entry(janela, font='Time 10')
inputEmail.place(width=250, height=20, x=100, y=270)

def ReceberEntries():

    nome = inputNome.get()
    telemovel = inputTelemovel.get()
    endereco = inputEndereco.get()
    distrito = inputDistrito.get()
    pais = inputPais.get()
    email = inputEmail.get()

    return nome,telemovel,endereco,distrito,pais,email

def LimparEntries():
    inputNome.delete('0', 'end')
    inputTelemovel.delete('0', 'end')
    inputEndereco.delete('0', 'end')
    inputDistrito.delete('0', 'end')
    inputPais.delete('0', 'end')
    inputEmail.delete('0', 'end')

def Adicionar():
    nome, telemovel, endereco, distrito, pais, email = ReceberEntries()

    with open('agenda.txt', 'a') as arquivo:
        arquivo.write(nome + '\n' + telemovel + '\n' + endereco + '\n' + distrito + '\n' + pais + '\n' + email + '\n' )
    
    messagebox.showinfo('Agenda', 'Cadastro Efetuado com Sucesso')

    LimparEntries()

def Procurar():
    pNome = inputNome.get()

    with open('agena.txt', 'r') as arquivo:
        for linha in arquivo:
            if pNome in linha:
                pTelemovel = (arquivo.readline())
                pEndereco = (arquivo.readline())
                pDistrito = (arquivo.readline())
                pPais = (arquivo.readline())
                pEmails = (arquivo.readline())

                labelNomeBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelNomeBusca.place(width=250, height=30, x=20, y=360)
                labelTelemovelBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelTelemovelBusca.place(width=250, height=30, x=20, y=380)
                labelEnderecoBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelEnderecoBusca.place(width=250, height=30, x=20, y=400)
                labelDistritoBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelDistritoBusca.place(width=100, height=30, x=20, y=420)
                labelPaisBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelPaisBusca.place(width=250, height=30, x=20, y=440)
                labelEmailBusca = Label(janela, text=linha, font='Times 10', anchor='w')
                labelEmailBusca.place(width=250, height=30, x=20, y=460)
                LimparEntries()
            else:
                messagebox.showerror('Agenda', 'Cadastro não encontrado!')
                break


buttonAdicionar = Button(janela, text='Adicionar', command=Adicionar, font='Times 10 bold', bg=blue, fg=white)
buttonAdicionar.place(width=80, height=30, x=70, y=310)

buttonProcurar = Button(janela, text='Adicionar', command=Adicionar, font='Times 10 bold', bg=blue, fg=white)
buttonProcurar.place(width=80, height=30, x=240, y=310)

janela.mainloop()