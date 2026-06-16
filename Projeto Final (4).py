from tkinter import ttk
from tkinter import *
from datetime import datetime
import requests
import tkintermapview

atual = datetime.now().strftime('%d-%m %H:%M')
lista = ['EUR', 'USD', 'BRL']

branco = '#ffffff'
azul = '#40596b'
vermelho = '#b53128'
preto = '#02040d'

janela = Tk()
janela.title(atual)
janela.geometry('250x350+500+100')
janela.wm_resizable(width=False, height=False)

janela2 = Tk()
janela2.title(atual)
janela2.geometry('250x350+500+100')
janela2.wm_resizable(width=False, height=False)

labelConversor = Label(janela, text='POKéMART', font='Time 16 bold', bg=branco, fg=vermelho, anchor='w', padx=15)
labelConversor.place(width=250, height=50, x=0, y=0)

labelPokéball = Label(janela, text='Pokéball', font='Time 11 bold', anchor='w')
labelPokéball.place(width=100, height=20, x=10, y=150)
moedaPokéball = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaPokéball.place(width=110, height=30, x=10, y=180)
moedaPokéball['values'] = (lista)

labelultraball = Label(janela, text='Ultraball', font='Time 11 bold', anchor='w')
labelultraball.place(width=100, height=20, x=260, y=150)
moedaultraball = ttk.Combobox(janela, font='Time 12 bold', justify=CENTER)
moedaultraball.place(width=110, height=30, x=260, y=180)
moedaultraball['values'] = (lista)

inputValor = ttk.Entry(janela, font='Time 12 bold', justify=CENTER)
inputValor.place(width=230, height=30, x=10, y=230)

def converter():

    Pokéball = pokemon.get()
    Greatball = pokemon2.get()
    Ultraball = pokemon3.get()
     
    lista_pk = requests.get(f'lista_pk"https://pokeapi.co/api/v2/type/" + tipo{id_pokemon}')
    lista_pk = lista_pk.json()
    cotacao_lista_pk = float(lista_pk[f'{id_pokemon}']['bid'])

    valor = float(inputValor.get())
    resultado = round(valor * cotacao_lista_pk,2)

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

buttonPokéMart = Button(janela, text='PokéMart', command=janela, font='Time 12 bold', bg=azul, fg=branco)
buttonPokéMart.place(width=230, height=30, x=10, y=300)

# -------------------------------------------------------------
janela.mainloop()