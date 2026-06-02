import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
from io import BytesIO

API_KEY = "3b3ddc5f98b8f6502b43eea92f40a73d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/"

def obterDadosMeteorologicos(cidade):
    params = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def guardarHistorico(cidade, temperatura):
    with open('historicoTemperaturas.txt', 'a', encoding='utf-8') as ficheiro:
        dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ficheiro.write(f"{dataHora} - {cidade}: {temperatura}°C\n") 

class AppMeteorologia:

    def _init_(self, janela):
        self.janela = janela
        self.janela.title("App de Meteorologia")
        self.janela.geometry("400x300")
        self.janela.configure(bg="#2E2E2E")
        
        self.cidadeLabel = tk.Label(janela, text="Cidade / País:", bg="#2E2E2E", fg="white")
        self.cidadeLabel.pack(pady=10)

        self.cidadeEntry = tk.Entry(janela, width=50)
        self.cidadeEntry.pack(pady=10)

        self.buscarButton = tk.Button(janela, text="Pesquisar", command=self.procurarMeteorologia, bg="white")
        self.buscarButton.pack(pady=10)

        self.resultadoLabel = tk.Label(janela, text="", wraplength=350, bg="#2E2E2E", fg="white")
        self.resultadoLabel.pack(pady=10)

        self.iconLabel = tk.Label(janela, bg="#2E2E2E")
        self.iconLabel.pack(pady=10)

    def procurarMeteorologia(self):
        cidade = self.cidadeEntry.get()
        if cidade:
            dados = obterDadosMeteorologicos(cidade)
            if dados.get("cod") != 200:
                messagebox.showerror("Erro", dados.get("message", "Erro ao procurar dados"))
            else:
                temperatura = dados["main"]["temp"]
                descricao = dados["weather"][0]["description"]
                iconCode = dados["weather"][0]["icon"]
                iconUrl = f"{ICON_URL}{iconCode}@2x.png"

                # Download da imagem do ícone
                response = requests.get(iconUrl)
                imgData = response.content
                img = Image.open(BytesIO(imgData))
                img = img.resize((100, 100), Image.LANCZOS)

                # Cria uma nova imagem com fundo cinza escuro
                background = Image.new('RGBA', img.size, (46, 46, 46, 255))
                img = Image.alpha_composite(background, img.convert('RGBA'))

                imgTk = ImageTk.PhotoImage(img)

                # Atualiza o ícone na interface
                self.iconLabel.config(image=imgTk)
                self.iconLabel.image = imgTk

                self.resultadoLabel.config(text=f"Temperatura: {temperatura}°C\nDescrição: {descricao.capitalize()}")
                guardarHistorico(cidade, temperatura)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade")

def main():
    janela = tk.Tk()
    app = AppMeteorologia(janela)
    janela.mainloop()

if __name__ == "_main_":
    main()
    