import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkintermapview
import random

# ==========================================
# CONSTANTES (APIs, Cores e Valores Fixos)
# ==========================================
API_POKE_URL = "https://pokeapi.co/api/v2/pokemon/"

COR_FUNDO_APP = "#CC0000"
COR_FUNDO_PAINEL = "#FFFFFF"
COR_FUNDO_DEX = "#2E2E2E"
COR_BOTAO_CATCH = "#FF4444"
COR_TEXTO_CLARO = "white"

CUSTO_POKEBOLAS = 20
RECOMPENSA_CATCH = 15

# ==========================================
# VARIÁVEIS DE ESTADO (Padrão camelCase)
# ==========================================
pokeDollars = 100
pokebolas = 5
inventario = {}
pokemonAtual = None
imagemAtual = None

# ==========================================
# LÓGICA DO JOGO
# ==========================================

def atualizarStatus():
    totalCapturados = sum(inventario.values())
    textoStatus = f"🪙 {pokeDollars}€  |  🔴 Bolas: {pokebolas}  |  🎒 Total: {totalCapturados}"
    labelStatus.config(text=textoStatus)

def comprarBolas():
    global pokeDollars, pokebolas
    
    if pokeDollars >= CUSTO_POKEBOLAS:
        pokeDollars -= CUSTO_POKEBOLAS
        pokebolas += 5
        atualizarStatus()
        messagebox.showinfo("PokéMart", "Compraste 5 Pokébolas!")
    else:
        messagebox.showwarning("PokéMart", "Não tens dinheiro suficiente!")

def explorarArea():
    global pokemonAtual, imagemAtual
    cidadeEscolhida = entryCidade.get()
    
    if not cidadeEscolhida:
        messagebox.showerror("Erro", "Escreve o nome de uma cidade!")
        return

    # 1. Atualizar o Mapa
    mapaWidget.set_address(cidadeEscolhida)
    mapaWidget.set_zoom(12)

    try:
        # 2. Procurar um Pokémon Aleatório (Geração 1: IDs 1 a 151)
        idAleatorio = random.randint(1, 151)
        urlBusca = f"{API_POKE_URL}{idAleatorio}"
        respostaApi = requests.get(urlBusca).json()
        
        pokemonAtual = respostaApi["name"].capitalize()

        # 3. Processar e Mostrar a Imagem
        urlImagem = respostaApi["sprites"]["other"]["official-artwork"]["front_default"]
        dadosImagem = requests.get(urlImagem).content
        imagemFormatada = Image.open(BytesIO(dadosImagem)).resize((130, 130))
        imagemAtual = ImageTk.PhotoImage(imagemFormatada)

        labelImagemPkmn.config(image=imagemAtual)
        labelEncontro.config(text=f"Um {pokemonAtual} selvagem apareceu em {cidadeEscolhida}!")
        btnCapturar.config(state="normal")
        
    except Exception as erro:
        print(erro)
        messagebox.showerror("Erro", "Falha ao contactar o radar Pokémon.")

def capturarPokemon():
    global pokebolas, pokemonAtual, pokeDollars

    if pokebolas <= 0:
        messagebox.showwarning("Aviso", "Sem Pokébolas! Vai à loja comprar mais.")
        return

    pokebolas -= 1

    # Sorteio simples de captura
    capturaSucesso = random.choice([True, True, False])

    if capturaSucesso:
        if pokemonAtual in inventario:
            inventario[pokemonAtual] += 1
        else:
            inventario[pokemonAtual] = 1
            
        pokeDollars += RECOMPENSA_CATCH
        messagebox.showinfo("Sucesso!", f"Capturaste o {pokemonAtual}!")
    else:
        messagebox.showerror("Oh não!", f"O {pokemonAtual} partiu a bola e fugiu!")

    # Limpar ecrã após tentativa
    labelImagemPkmn.config(image="")
    labelEncontro.config(text="Procura noutra cidade...")
    btnCapturar.config(state="disabled")
    pokemonAtual = None
    
    atualizarStatus()

# ==========================================
# POKÉDEX (NOVA JANELA)
# ==========================================

def abrirPokedex():
    janelaDex = tk.Toplevel()
    janelaDex.title("Pokédex")
    janelaDex.geometry("300x350")
    janelaDex.configure(bg=COR_FUNDO_DEX)
    
    labelTitulo = tk.Label(janelaDex, text="📖 A Tua Pokédex", font=("Arial", 14, "bold"), bg=COR_FUNDO_DEX, fg=COR_TEXTO_CLARO)
    labelTitulo.pack(pady=10)
    
    listaDex = tk.Listbox(janelaDex, font=("Arial", 12))
    listaDex.pack(fill="both", expand=True, padx=20, pady=10)
    
    for nomePkmn, quantidadePkmn in inventario.items():
        listaDex.insert(tk.END, f"{nomePkmn} (Quantidade: {quantidadePkmn})")

# ==========================================
# INTERFACE GRÁFICA PRINCIPAL
# ==========================================

def desenharInterface():
    global janelaPrincipal, labelStatus, entryCidade, mapaWidget
    global labelImagemPkmn, labelEncontro, btnCapturar

    janelaPrincipal = tk.Tk()
    janelaPrincipal.title("PokéDex Global - Aula")
    janelaPrincipal.geometry("600x750")
    janelaPrincipal.configure(bg=COR_FUNDO_APP)

    # --- Barra de Status ---
    frameStatus = tk.Frame(janelaPrincipal, bg=COR_FUNDO_PAINEL, bd=3, relief="ridge")
    frameStatus.pack(pady=10, fill="x", padx=10)
    
    labelStatus = tk.Label(frameStatus, font=("Arial", 12, "bold"), bg=COR_FUNDO_PAINEL)
    labelStatus.pack(pady=5)

    # --- Topo: Pesquisa ---
    frameTopo = tk.Frame(janelaPrincipal, bg=COR_FUNDO_APP)
    frameTopo.pack(pady=5)
    
    labelCidade = tk.Label(frameTopo, text="Cidade:", bg=COR_FUNDO_APP, fg=COR_TEXTO_CLARO, font=("Arial", 12, "bold"))
    labelCidade.grid(row=0, column=0, padx=5)
    
    entryCidade = tk.Entry(frameTopo, font=("Arial", 12))
    entryCidade.grid(row=0, column=1, padx=5)
    
    btnExplorar = tk.Button(frameTopo, text="🌍 Explorar", command=explorarArea, font=("Arial", 10, "bold"))
    btnExplorar.grid(row=0, column=2, padx=5)

    # --- Mapa ---
    frameMapa = tk.Frame(janelaPrincipal, bd=3, relief="sunken")
    frameMapa.pack(pady=10)
    
    mapaWidget = tkintermapview.TkinterMapView(frameMapa, width=500, height=200)
    mapaWidget.pack()
    mapaWidget.set_position(39.3999, -8.2245) # Coordenadas padrão
    mapaWidget.set_zoom(6)

    # --- Área de Captura ---
    frameCombate = tk.Frame(janelaPrincipal, bg=COR_FUNDO_PAINEL, bd=5)
    frameCombate.pack(pady=10, fill="x", padx=25)
    
    labelImagemPkmn = tk.Label(frameCombate, bg=COR_FUNDO_PAINEL)
    labelImagemPkmn.pack(pady=5)
    
    labelEncontro = tk.Label(frameCombate, text="Escreve uma cidade e clica em Explorar...", bg=COR_FUNDO_PAINEL, font=("Arial", 12))
    labelEncontro.pack(pady=5)
    
    btnCapturar = tk.Button(frameCombate, text="🔴 LANÇAR POKéBOLA", command=capturarPokemon, state="disabled", font=("Arial", 14, "bold"), bg=COR_BOTAO_CATCH, fg=COR_TEXTO_CLARO)
    btnCapturar.pack(pady=10)

    # --- Botões Inferiores ---
    frameBotoes = tk.Frame(janelaPrincipal, bg=COR_FUNDO_APP)
    frameBotoes.pack(pady=10)
    
    btnLoja = tk.Button(frameBotoes, text=f"🛒 COMPRAR POKéBOLAS ({CUSTO_POKEBOLAS}€)", command=comprarBolas, bg="lightblue", font=("Arial", 10, "bold"))
    btnLoja.grid(row=0, column=0, padx=10)
    
    btnDex = tk.Button(frameBotoes, text="📖 ABRIR POKéDEX", command=abrirPokedex, bg="blue", fg=COR_TEXTO_CLARO, font=("Arial", 10, "bold"))
    btnDex.grid(row=0, column=1, padx=10)

    # Iniciar o jogo e abrir a janela
    atualizarStatus()
    janelaPrincipal.mainloop()

# ==========================================
# INÍCIO DO PROGRAMA
# ==========================================
if __name__ == "__main__":
    desenharInterface()
