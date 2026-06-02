from tkinter import ttk
from tkinter import *
from datetime import datetime
import requests

# -------------------------------------------------------------

atual = datetime.now().strftime('%d-%m %H:%M')
lista = ['EUR', 'USD', 'BRL']

# -------------------------------------------------------------
# cor

branco = '#ffffff'
azul = '#40596b'
vermelho = '#b53128'
preto = '#02040d'

# -------------------------------------------------------------
# tela

janela = Tk()
janela.title(atual)
janela.geometry('250x350+500+100')
janela.wm_resizable(width=False, height=False)

# labels e entrys

labelConversor = Label(janela, text='Conversor de Moeda', font='Time 16 bold', bg=azul, fg=branco, anchor='w', padx=15)
labelConversor.place(width=250, height=50, x=0, y=0)

labelMoedaDe = Label(janela, text='De', font='Time 11 bold', anchor='w')
labelMoedaDe.place(width=100, height=20, x=10, y=150)
moedaDe = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaDe.place(width=110, height=30, x=10, y=180)
moedaDe['values'] = (lista)

labelMoedaPara = Label(janela, text='Para', font='Time 11 bold', anchor='w')
labelMoedaPara.place(width=100, height=20, x=130, y=150)
moedaPara = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaPara.place(width=110, height=30, x=130, y=180)
moedaPara['values'] = (lista)

inputValor = ttk.Entry(janela, font='Time 12 bold', justify=CENTER)
inputValor.place(width=230, height=30, x=10, y=230)

# -------------------------------------------------------------
# funções

def converter():

    de = moedaDe.get()
    para = moedaPara.get()

    # request
    cotacao = requests.get(f'https://economia.awesomeapi.com.br/last/{de}-{para}')
    cotacao = cotacao.json()
    cotacaoMoeda = float(cotacao[f'{de}{para}']['bid'])

    #formula

    valor = float(inputValor.get())
    resultado = round(valor * cotacaoMoeda,2)

    #simbolos

    if para == 'EUR':
        simbolo = '€'
    elif para == 'USD':
        simbolo = 'US$'
    else:
        simbolo = 'R$'

    labelConversor = Label(janela, text=(simbolo,resultado), font='Time 16 bold', fg=vermelho, anchor='w', padx=5)
    labelConversor.place(width=200, height=40, x=25, y=75)

# -------------------------------------------------------------
# botões

buttonAdicionar = Button(janela, text='Converter', command=converter, font='Time 12 bold', bg=azul, fg=branco)
buttonAdicionar.place(width=230, height=30, x=10, y=300)

# -------------------------------------------------------------
janela.mainloop()