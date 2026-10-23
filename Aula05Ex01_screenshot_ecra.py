import os
import pyautogui
from time import sleep
from datetime import datetime

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


# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 05A — Screenshot do Ecrã Inteiro (Versão Robusta)
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Tirar uma fotografia ao ecrã inteiro e guardar
#   no Desktop com nome automático que inclui data e hora.
# ═══════════════════════════════════════════════════════════

# 🔎 LÓGICA DE DETEÇÃO DO DESKTOP (Solução para o erro FileNotFoundError)
desktop = get_desktop()

# ── CONFIGURAÇÃO DO FICHEIRO ────────────────────────────────
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arq = f"screenshot_{agora}.png"
caminho = os.path.join(desktop, nome_arq)

print("═" * 60)
print(f"🖥️  Resolução do Ecrã: {pyautogui.size()}")
print(f"📂 Pasta de destino: {desktop}")
print(f"📄 Nome do ficheiro: {nome_arq}")
print("═" * 60)

print("\nPrepara o ecrã que queres capturar...")
print("A tirar screenshot em 3 segundos...\n")
sleep(3)

# ── EXECUÇÃO ────────────────────────────────────────────────

# 1. Tirar screenshot (Requer biblioteca Pillow instalada!)
print("📸 Click! Screenshot capturado.")
imagem = pyautogui.screenshot()

# 2. Informação sobre a imagem
largura, altura = imagem.size
print(f"📊 Dimensões: {largura}×{altura} píxeis")

# 3. Guardar no Desktop (ou pasta detetada)
try:
    imagem.save(caminho)

    # 4. Verificar que foi guardado
    if os.path.exists(caminho):
        tamanho = os.path.getsize(caminho)
        print(f"\n✅ SUCESSO: Screenshot guardado em:")
        print(f"👉 {caminho}")
        print(f"📦 Tamanho: {tamanho:,} bytes")
    else:
        print("\n⚠ Erro: O ficheiro não foi encontrado após a gravação.")

except Exception as e:
    print(f"\n❌ Erro crítico ao guardar: {e}")
    print("Dica: Verifica se tens permissões de escrita na pasta.")

# Abre a pasta do Windows e destaca o ficheiro que acabámos de criar
os.startfile(desktop)
# OU, para abrir a imagem diretamente:
# os.startfile(caminho)
print("\n" + "═" * 60)
print("Próximo: ex05b para capturar uma região específica.")

# ── DESAFIO ────────────────────────────────────────────────
# Tira 3 screenshots com 2 segundos de intervalo:

for i in range(1, 4):
    sleep(2)
    img = pyautogui.screenshot()
    caminh = os.path.join(desktop, f"screenshot_{i:02d}.png")
    img.save(caminh)
    print(f'Screenshot {i} tirado!')
