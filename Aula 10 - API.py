from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests

atual = datetime.now().strftime('%d-%m %H:%M')
lista = ['EUR', 'USD', 'BRL']

branco = '#ffffff'
azul = '#40596b'
vermelho = '#b53128'
preto = '#02040d'

janela = Tk()
janela.title(atual)
janela.geometry('300x350+500+100')
janela.wm_resizable(width=False, height=False)

labelConversor = Label(janela, text='Conversor de Moeda', font='Time 20 bold', bg=azul, fg=branco, anchor='w', padx=10)
labelConversor.place(width=380, height=50, x=0, y=0)

labelDe = Label(janela, text='De', font='Time 15', anchor='w')
labelDe.place(width=60, height=20, x=10, y=150)

labelPara = Label(janela, text='Para', font='Time 15', anchor='w')
labelPara.place(width=60, height=20, x=150, y=150)

moedaDe = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaDe.place(width=110, height=30 , x=10, y=180)
moedaDe['values'] = (lista)

moedaPara = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaPara.place(width=110, height=30 , x=150, y=180)
moedaPara['values'] = (lista)

inputValor = ttk.Entry(janela, font='Time 12 bold', justify=CENTER)
inputValor.place(width=230, height=30, x=10, y=230)

def converter():
    de = moedaDe.get()
    para = moedaPara.get()

    cotacao = requests.get(f'https://economia.awesomeapi.com.br/last/{de}-{para}')
    cotacao = cotacao.json()
    cotacaoMoeda = float(cotacao[f'{de}{para}']['bid'])

    valor = float(inputValor.get())
    resultado = round(valor * cotacaoMoeda,2)

    if para == 'EUR':
        simbolo = '€'
    elif para == 'USD':
        simbolo = 'US$'
    else:
        simbolo = 'R$'
    
    labelConversor = Label(janela, text='Converter', command=converter, font='Time 12 bold', bg=azul, fg=branco)
    labelConversor.place(width=230, height=30, x=10, y=300)

buttonAdicionar = Button(janela, text='Converter', command=converter, font='Times 12 bold', bg=azul, fg=branco)
buttonAdicionar.place(width=230, height=30, x=10, y=300)

janela.mainloop()