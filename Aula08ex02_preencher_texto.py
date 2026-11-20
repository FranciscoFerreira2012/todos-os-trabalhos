import pyautogui
import pyperclip
from time import sleep
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 08B — Preencher Campos de Texto no Formulário
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Com o formulário do ex08a aberto, preencher
#   os campos de texto curto e longo usando Tab para navegar
#   e pyperclip para textos com acentos.
#   PRÉ-REQUISITO: ex08a concluído (formulário visível).
#
# ESTRATÉGIA DE NAVEGAÇÃO NUM FORMULÁRIO:
#   Tab     → avança para o próximo campo
#   Shift+Tab → volta ao campo anterior
#   Enter   → pode submeter — CUIDADO!
#   Ctrl+A  → selecionar tudo no campo atual
#
# COMO DESCOBRIR A ORDEM DOS CAMPOS:
#   1. Abre o formulário no browser
#   2. Usa o ex01b para descobrir coordenadas do 1.º campo
#   3. Usa Tab para navegar entre campos sem coordenadas
#
# ⚠ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
# Coordenadas do PRIMEIRO campo do formulário (ex02b)
X_PRIMEIRO_CAMPO = None   # ← descobre com o ex01b
Y_PRIMEIRO_CAMPO = None

# Dados a preencher (personaliza com os teus dados!)
agora = datetime.now().strftime('%d/%m/%Y %H:%M')
DADOS = {
    "nome":      "Aluno SharkCoders",
    "email":     "aluno@sharkcoders.pt",
    "mensagem":  f"Formulário preenchido automaticamente com Python!\nData: {agora}\nFeito com PyAutoGui 🤖",
    "numero":    "123",
}
# ────────────────────────────────────────────────────────────

if X_PRIMEIRO_CAMPO is None:
    print("⚠ Preenche X_PRIMEIRO_CAMPO e Y_PRIMEIRO_CAMPO com o ex01b!")
    print("  Aponta para o centro do 1.º campo de texto do formulário.")
    exit()

print("Dados a preencher:")
for k, v in DADOS.items():
    print(f"  {k}: {v[:50]}")

print("\nA iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# Passo 1 — Clicar no primeiro campo
print("Passo 1: A focar o primeiro campo...")
pyautogui.click(X_PRIMEIRO_CAMPO, Y_PRIMEIRO_CAMPO)
sleep(0.5)

# Passo 2 — Preencher nome (sem acentos → write)
print("Passo 2: A preencher nome...")
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(DADOS["nome"], interval=0.04)
sleep(0.3)

# Passo 3 — Tab para próximo campo (email)
print("Passo 3: A preencher email...")
pyautogui.press('tab')
sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(DADOS["email"], interval=0.04)
sleep(0.3)

# Passo 4 — Tab para campo numérico
print("Passo 4: A preencher número...")
pyautogui.press('tab')
sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(DADOS["numero"], interval=0.05)
sleep(0.3)

# Passo 5 — Tab para campo de texto longo (COM acentos → pyperclip)
print("Passo 5: A preencher mensagem com acentos...")
pyautogui.press('tab')
sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy(DADOS["mensagem"])
pyautogui.hotkey('ctrl', 'v')
sleep(0.3)

print("\n✓ Campos de texto preenchidos!")
print("Próximo: ex08c para selecionar opções (radio, checkbox, dropdown).")

# ── DESAFIO ────────────────────────────────────────────────
# Pede os dados ao utilizador ANTES do sleep(3):