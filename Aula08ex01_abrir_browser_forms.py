import pyautogui
import pyperclip
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 07A — Abrir Browser e Navegar para Google Forms
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Abrir o browser com Win+R e navegar para o URL
#   do Google Form configurado pelo professor.
#   Este é o ponto de entrada para todos os ex08b/c/d.
#
# CONCEITOS NOVOS:
#   Win+R → chrome/firefox/msedge — abrir browser
#   Barra de endereços com Ctrl+L  — focar endereço
#   pyperclip para URL            — evitar erros de escrita
#   sleep() progressivo           — aguardar carregamento
#
# ⚠ ANTES DE CORRER:
#   1. o professor tem que ter o URL do Google Form
#   2. Substituir FORM_URL abaixo
#   3. Confirmar qual é o teu browser (BROWSER abaixo)
#
# ⚠ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
FORM_URL = "https://docs.google.com/forms/u/0/"
BROWSER  = "brave"   # "chrome" | "firefox" | "msedge"
# ────────────────────────────────────────────────────────────

if "SUBSTITUIR" in FORM_URL:
    print("⚠ Preenche FORM_URL com o URL fornecido pelo professor!")
    exit()

print(f"Browser: {BROWSER}")
print(f"URL: {FORM_URL[:60]}...")
print("\nA iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Passo 1 — Abrir browser com Win+R
print("Passo 1: A abrir browser...")
pyautogui.hotkey('win', 'r')
sleep(0.8)
pyautogui.write(BROWSER, interval=0.05)
pyautogui.press('enter')
sleep(2.5)   # aguardar browser abrir completamente

# Passo 2 — Focar barra de endereços e navegar
print("Passo 2: A navegar para o formulário...")
pyautogui.hotkey('ctrl', 'l')    # focar barra de endereços
sleep(0.5)
pyperclip.copy(FORM_URL)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(3.0)   # aguardar página carregar

# Passo 3 — Verificar (visual — não temos locateOnScreen ainda)
print("Passo 3: A verificar carregamento...")
print("  (Confirma visualmente que o formulário carregou)")
sleep(1.0)

print("\n✓ Browser aberto e formulário carregado!")
print("Próximo: ex08b para preencher os campos de texto.")

# ── DESAFIO ────────────────────────────────────────────────
# Abre o formulário numa janela com tamanho específico:
import pygetwindow as gw
janelas = gw.getWindowsWithTitle('Chrome') or gw.getWindowsWithTitle('Google')
if janelas:
    janelas[0].resizeTo(1200, 800)
    janelas[0].moveTo(100, 50)