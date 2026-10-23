# ── IMPORTAÇÃO DE BIBLIOTECAS ────────────────────────────────
import os             # Para interagir com o sistema operativo (abrir ficheiros, fechar programas)
import pyautogui      # Para simular o rato e o teclado do utilizador
from time import sleep # Para criar pausas e dar tempo ao computador de processar as ações
from datetime import date # Para conseguir obter a data atual do sistema

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 02D — Abrir Ficheiro e Escrever Conteúdo
# ═══════════════════════════════════════════════════════════

# Segurança extra: se o rato for arrastado rapidamente para um dos cantos do ecrã, o programa para.
pyautogui.FAILSAFE = True

# ── FUNÇÃO PARA ENCONTRAR O DESKTOP ───────────────────────
# Esta função procura a pasta do "Ambiente de Trabalho" independentemente de o
# Windows estar em PT, EN, ou se tem o OneDrive ativado.
def get_desktop():
    u = os.environ["USERPROFILE"] # Pega no caminho base do utilizador (ex: C:\Users\Joao)
    candidatos = [
        os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive - sharkcoders", "Desktop"),
        os.path.join(u, "OneDrive", "Desktop"),
        os.path.join(u, "Desktop"),
        os.path.join(u, "Ambiente de Trabalho"),
    ]
    # Testa os caminhos um a um e devolve o primeiro que realmente existir no PC
    return next((c for c in candidatos if os.path.exists(c)), u)

# ── VERIFICAÇÃO DO FICHEIRO ───────────────────────────────
desktop = get_desktop()
caminho = os.path.join(desktop, "Teste Python.txt") # Junta a pasta com o nome do ficheiro

# Se o ficheiro não existir na pasta, avisa o utilizador e cancela a execução (exit)
if not os.path.exists(caminho):
    print("\n⚠️ Ficheiro 'Teste Python.txt' não encontrado!")
    print("  Completa o ex02c primeiro.")
    print(f"  Caminho esperado: {caminho}")
    exit()

print(f"✓ Ficheiro encontrado: {caminho}")

# Tempo de espera para que o utilizador consiga minimizar o PyCharm antes da automação começar
print("\nA iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# ── AUTOMAÇÃO (PASSOS) ────────────────────────────────────

# Passo 1 — Abrir o ficheiro diretamente pelo Windows
print("Passo 1: A abrir o ficheiro...")
os.startfile(caminho) # É o equivalente a dar duplo clique, mas feito internamente pelo sistema
sleep(2) # Espera 2 segundos para dar tempo ao Bloco de Notas de abrir completamente

# Passo 2 — Cursor no início do texto
print("Passo 2: A posicionar cursor...")
pyautogui.hotkey('ctrl', 'home') # Atalho que leva o cursor para a primeira linha do documento
sleep(0.3)

# Passo 3 — Escrever linha a linha
print("Passo 3: A escrever texto...")
hoje = date.today().strftime("%d/%m/%Y") # Vai buscar a data de hoje e formata para Dia/Mês/Ano

# Lista de frases a serem escritas
linhas = [
    "Ola, sou um bot feito com Python!",
    f"Data: {hoje}",
    "Feito com: pyautogui",
]

# Ciclo que percorre cada frase da lista
for linha in linhas:
    pyautogui.write(linha, interval=0.03) # Escreve o texto com uma pausa de 0.03s por letra (simula um humano)
    pyautogui.press('enter')               # Carrega no Enter para mudar de linha
    sleep(0.2)                             # Pequena pausa antes de começar a escrever a próxima linha

# Passo 4 — Guardar o documento
print("Passo 4: A guardar...")
pyautogui.hotkey('ctrl', 's') # Atalho universal para Guardar (Save)
sleep(1)                      # Dá tempo ao disco para guardar o ficheiro fisicamente

# Passo 5 — Fechar a aplicação com segurança
print("Passo 5: A encerrar o Notepad...")
# Usamos o taskkill para matar o processo diretamente no Windows. 
# Isto impede que o computador tente encerrar o PyCharm ou desligar o Windows (o que poderia acontecer com Alt+F4 se a janela perdesse o foco)
os.system("taskkill /f /im notepad.exe")

print("\n✓ Ficheiro escrito, guardado e fechado!")
print("Parabéns — completaste todos os exercícios da Aula 02! 🎉")