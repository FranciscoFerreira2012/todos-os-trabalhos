import pyautogui
import pygetwindow as gw
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 07C — Abrir 3 Apps e Organizar Lado a Lado
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Abrir Notepad, Paint e Calculadora com Win+R
#   e organizá-las automaticamente em 3 colunas iguais.
#   PRÉ-REQUISITO: ex06b concluído.
#
# CONCEITOS NOVOS:
#   Calcular layout por código    — dividir ecrã em colunas
#   Combinar Win+R com pygetwindow— abrir E posicionar
#   Loop sobre lista de janelas   — tratar múltiplas janelas
#
# FIO CONDUTOR: estas 3 janelas vão ser monitorizadas no 06d.
#
# ⚠ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# Obter tamanho do ecrã
LARG, ALT = pyautogui.size()
MARGEM    = 10
COL_LARG  = (LARG - MARGEM * 4) // 3   # 3 colunas com margens
COL_ALT   = ALT - 80                   # deixar espaço para taskbar

ROW_ALT = (ALT - MARGEM * 3 - 80) // 2
ROW_LARG = LARG - MARGEM * 2
posicoes = [(MARGEM, MARGEM), (MARGEM, MARGEM + ROW_ALT + MARGEM)]

# Definir apps a abrir: (comando Win+R, título a procurar, pesquisa alternativa)
APPS = [
    ("notepad",  ["Notepad", "Bloco de Notas", "Untitled"]),
    ("chrome",  ["Chrome", "tab"]),
    ("calc",     ["Calculadora", "Calculator"]),
]

print(f"Ecrã: {LARG}×{ALT}px")
print(f"Layout: 3 colunas de {COL_LARG}×{COL_ALT}px\n")
print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# ── Passo 1 — Abrir as 3 apps ───────────────────────────────
for cmd, _ in APPS:
    print(f"A abrir {cmd}...")
    pyautogui.hotkey('win', 'r')
    sleep(0.8)
    pyautogui.write(cmd, interval=0.05)
    pyautogui.press('enter')
    sleep(1.5)   # aguardar app inicializar

sleep(1.0)   # pausa extra para garantir que todas abriram

# ── Passo 2 — Localizar e posicionar cada app ───────────────
print("\nA organizar janelas...")
posicionadas = []

for i, (cmd, titulos) in enumerate(APPS):
    # Calcular posição desta coluna
    x = MARGEM + i * (ROW_ALT + MARGEM)
    y = MARGEM

    # Procurar a janela por qualquer dos títulos
    janela = None
    for titulo in titulos:
        resultados = gw.getWindowsWithTitle(titulo)
        if resultados:
            janela = resultados[0]
            break

    if janela is None:
        print(f"  ⚠ {cmd} não encontrado — a continuar...")
        continue

    # Restaurar, mover e redimensionar
    try:
        janela.restore()
        sleep(0.3)
        janela.activate()
        sleep(0.3)
        janela.moveTo(x, y)
        sleep(0.3)
        janela.resizeTo(COL_LARG, COL_ALT)
        sleep(0.3)
        posicionadas.append((cmd, janela, x, y, COL_LARG, COL_ALT))
        print(f"  ✓ {cmd:10} → coluna {i+1} em ({x},{y}) {COL_LARG}×{COL_ALT}px")
    except Exception as e:
        print(f"  ⚠ Erro com {cmd}: {e}")

print(f"\n✓ {len(posicionadas)}/3 apps organizadas lado a lado!")
print("Próximo: ex07d para monitorizar e manter o layout automaticamente.")

# ── DESAFIO ────────────────────────────────────────────────
# Experimenta 2 linhas em vez de 3 colunas:
