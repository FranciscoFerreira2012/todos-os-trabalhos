import os
import pyautogui
import pyperclip
import pygetwindow as gw
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 02C — Renomear Ficheiro no Desktop com PyAutoGui
# ═══════════════════════════════════════════════════════════
# OBJETIVO: O bot vai:
#   1. Verificar que o ficheiro do ex01a existe
#   2. Abrir o Explorador de Ficheiros no Desktop
#   3. Activar a janela e clicar no ficheiro
#   4. Premir F2 para renomear
#   5. Escrever o novo nome e confirmar
#
# PRÉ-REQUISITO: ex02a concluído
#   ("Novo Documento de Texto.txt" deve existir no Desktop)
#
# CONCEITOS NOVOS:
#   pyperclip.copy()         — copiar texto para o clipboard
#   hotkey('ctrl','v')       — colar do clipboard
#   pygetwindow.activate()   — trazer janela para a frente
#   moveTo(x, y, duration)   — mover o rato visivelmente
#   press('f2')              — tecla de renomear no Windows
#
# ⚠️ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05   # pequena pausa entre cada acção do PyAutoGui

# ── Encontrar o Desktop real (funciona com e sem OneDrive) ──
def get_desktop():
    u = os.environ["USERPROFILE"]
    candidatos = [
        os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive - sharkcoders", "Desktop"),
        os.path.join(u, "OneDrive", "Desktop"),
        os.path.join(u, "Desktop"),
        os.path.join(u, "Ambiente de Trabalho"),
    ]
    return next((c for c in candidatos if os.path.exists(c)), u)

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
NOME_ANTIGO = "Novo Documento de Texto.txt"
NOME_NOVO   = "Teste Python"   # sem .txt — o Windows mantém a extensão
# ────────────────────────────────────────────────────────────

# ── PARTE 1 — Verificar pré-requisito (Python puro) ──────────
desktop        = get_desktop()
caminho_antigo = os.path.join(desktop, NOME_ANTIGO)
caminho_novo   = os.path.join(desktop, NOME_NOVO + ".txt")

print("=" * 50)
print("  EXERCÍCIO 02C — Renomear Ficheiro")
print("=" * 50)
print(f"\n📁 Desktop: {desktop}")

if not os.path.exists(caminho_antigo):
    print(f"\n⚠️ Ficheiro não encontrado: {NOME_ANTIGO}")
    print("  Corre primeiro o ex01a para criar o ficheiro.")
    exit()

if os.path.exists(caminho_novo):
    print(f"\n⚠️ Já existe um ficheiro chamado: {NOME_NOVO}.txt")
    print("  Apaga-o primeiro ou muda o NOME_NOVO neste ficheiro.")
    exit()

print(f"\n✓ Ficheiro encontrado : {NOME_ANTIGO}")
print(f"  Novo nome           : {NOME_NOVO}.txt")

# ── PARTE 2 — Renomear com PyAutoGui ─────────────────────────
print("\n" + "-" * 50)
print("  A iniciar em 3 segundos...")
print("  >> MINIMIZA o PyCharm agora! <<")
print("-" * 50)
for i in range(3, 0, -1):
    print(f"  {i}...")
    sleep(1)
print()

# Passo 1 — Abrir o Explorador directamente na pasta do Desktop
print("[ PASSO 1 ] A abrir o Explorador no Desktop...")
print(f"  hotkey('win', 'r')  → abre caixa Executar")
pyautogui.hotkey('win', 'r')
sleep(0.8)

print(f"  A colar o caminho: {desktop}")
pyperclip.copy(desktop)
pyautogui.hotkey('ctrl', 'v')
sleep(0.3)

print(f"  press('enter')  → abre o Explorador")
pyautogui.press('enter')
print("  A aguardar que o Explorador carregue...")
sleep(3.0)

# Passo 2 — Activar a janela do Explorador e clicar no centro
print("\n[ PASSO 2 ] A activar a janela do Explorador...")
janela = None
for titulo in ["Ambiente de Trabalho", "Desktop"]:
    encontradas = gw.getWindowsWithTitle(titulo)
    if encontradas:
        janela = encontradas[0]
        break

if janela:
    print(f"  ✓ Janela encontrada: '{janela.title}'")
    print(f"    Posição: x={janela.left}, y={janela.top}")
    print(f"    Tamanho: {janela.width}×{janela.height}")
    janela.activate()
    sleep(0.8)

    # Mover o rato visivelmente até ao centro da janela
    cx = janela.left + janela.width  // 2
    cy = janela.top  + janela.height // 2
    print(f"  moveTo({cx}, {cy})  → a mover o rato para o centro da janela")
    pyautogui.moveTo(cx, cy, duration=1.0)   # movimento lento e visível
    sleep(0.3)
    print(f"  click()  → a clicar para garantir foco")
    pyautogui.click(cx, cy)
    sleep(0.5)
else:
    print("  ⚠️ Janela não encontrada pelo título — a tentar continuar...")
    sleep(0.5)

# Passo 3 — Navegar para o ficheiro escrevendo as primeiras letras
print("\n[ PASSO 3 ] A navegar para o ficheiro...")
print("  write('Novo')  → escrever letras no Explorador selecciona o ficheiro")
pyautogui.write('Novo', interval=0.2)
sleep(1.0)
print("  ✓ Ficheiro 'Novo Documento de Texto.txt' seleccionado")

# Passo 4 — F2 para activar o modo de renomear
print("\n[ PASSO 4 ] A activar modo de renomear...")
print("  press('f2')  → F2 é o atalho do Windows para renomear")
pyautogui.press('f2')
sleep(0.6)
print("  ✓ Campo de nome activo — pronto para escrever")

# Passo 5 — Seleccionar o nome actual e colar o novo
print("\n[ PASSO 5 ] A escrever o novo nome...")
print("  hotkey('ctrl','a')  → seleccionar o nome actual")
pyautogui.hotkey('ctrl', 'a')
sleep(0.2)
print(f"  A copiar '{NOME_NOVO}' para o clipboard...")
pyperclip.copy(NOME_NOVO)
print("  hotkey('ctrl','v')  → colar o novo nome")
pyautogui.hotkey('ctrl', 'v')
sleep(0.2)
print(f"  ✓ Novo nome escrito: {NOME_NOVO}")

# Passo 6 — Confirmar com Enter
print("\n[ PASSO 6 ] A confirmar o novo nome...")
print("  press('enter')  → confirmar e sair do modo de renomear")
pyautogui.press('enter')
sleep(0.8)

# Passo 7 — Fechar o Explorador
print("\n[ PASSO 7 ] A fechar o Explorador...")
print("  hotkey('alt','f4')  → fechar a janela")
pyautogui.hotkey('alt', 'f4')
sleep(0.5)

# ── PARTE 3 — Confirmar que funcionou (Python puro) ──────────
print("\n" + "=" * 50)
if os.path.exists(caminho_novo):
    print("  ✓ SUCESSO — Ficheiro renomeado!")
    print(f"    Antes : {NOME_ANTIGO}")
    print(f"    Agora : {NOME_NOVO}.txt")
    print("\n  Próximo: ex02d para abrir e escrever dentro do ficheiro.")
else:
    print("  ⚠️ Algo correu mal — o ficheiro não foi renomeado.")
    print("  Verifica se o Explorador abriu correctamente.")
    print("  Tenta correr o exercício de novo.")
print("=" * 50)

# ── DESAFIO ────────────────────────────────────────────────
# 1. Pede o novo nome ao utilizador ANTES do sleep(3):
#    NOME_NOVO = input("Qual é o novo nome? ")
#    (tem de ser ANTES do sleep — depois o PyCharm está minimizado!)
#
# 2. Renomeia 3 ficheiros de uma vez com um ciclo for:
#    pares = [
#        ("Ficheiro1.txt", "Python1"),
#        ("Ficheiro2.txt", "Python2"),
#        ("Ficheiro3.txt", "Python3"),
#    ]
#    for antigo, novo in pares:
#        os.rename(os.path.join(desktop, antigo),
#                  os.path.join(desktop, novo + ".txt"))
#        print(f"✓ {antigo} → {novo}.txt")