import os
import pyautogui
import pyperclip
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
        os.path.join(u, "Documents", "aula03.txt"), 
        os.path.join(u, "Ambiente de Trabalho"),
    ]
    return next((c for c in candidatos if os.path.exists(c)), u)


# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 04D — Guardar Arte como PNG (Versão Final Blindada)
# ═══════════════════════════════════════════════════════════

# Segurança: Arrastar o rato para o canto do ecrã para o script!
pyautogui.FAILSAFE = True

# ── 1. PREPARAÇÃO DOS DADOS ─────────────────────────────────

# Localizar o Desktop automaticamente
desktop = get_desktop()
hoje = datetime.now().strftime('%Y-%m-%d_%H-%M')

# Nome padrão
nome_png = f"arte_final_{hoje}.png"

# Interface simples para o aluno
print("═" * 60)
print("💾 SISTEMA DE GRAVAÇÃO AUTOMÁTICA".center(60))
print("═" * 60)

titulo = input("\nNome da obra (Enter para padrão): ").strip()
if titulo:
    nome_png = f"{titulo.replace(' ', '')}{hoje}.png"

# Caminho completo que o robô vai escrever
destino = os.path.join(desktop, nome_png)

print(f"\n🚀 Destino: {destino}")
print("A iniciar em 3 segundos... PREPARA O PAINT!")
sleep(3)

# ── 2. ABRIR JANELA E FORÇAR FOCO ───────────────────────────

print("Passo 1: A chamar 'Guardar Como'...")
# O Windows 11 às vezes ignora o primeiro comando se estiver "a dormir"
pyautogui.hotkey('f12')
sleep(2.5) # Tempo essencial para a animação da janela do Win11

# TRUQUE DE FOCO: Clica no centro do ecrã para ativar a janela de gravação
largura, altura = pyautogui.size()
pyautogui.click(largura // 2, altura // 2)
sleep(0.5)

# ── 3. ESCREVER O CAMINHO (MÉTODO SEGURO) ───────────────────

print("Passo 2: A definir nome do ficheiro...")

# Limpar o campo de texto completamente
pyautogui.hotkey('ctrl', 'a')
sleep(0.3)
pyautogui.press('backspace')
sleep(0.5)

# Colar o caminho completo usando a Área de Transferência
pyperclip.copy(destino)
pyautogui.hotkey('ctrl', 'v')
sleep(1.0) # Dá tempo ao Paint para processar o texto colado

# ── 4. CONFIRMAR E LIDAR COM AVISOS ─────────────────────────

print("Passo 3: A confirmar gravação...")

# Primeiro Enter para gravar
pyautogui.press('enter')
sleep(1.5)

# Segundo Enter de segurança:
# Se aparecer "Deseja substituir?", este Enter clica em "Sim".
# Se não aparecer, este Enter não faz mal nenhum.
pyautogui.press('enter')
sleep(2.0) # Espera o disco rígido escrever o ficheiro

# ── 5. FECHAR E VERIFICAR ───────────────────────────────────

print("Passo 4: A encerrar o Paint...")
pyautogui.hotkey('alt', 'f4')
sleep(1.0)

# Se o Paint ainda perguntar se quer guardar (porque algo falhou), dizemos "Não"
# O Tab move para o botão "Não Guardar" e o Enter confirma.
pyautogui.press('tab')
pyautogui.press('enter')

# VERIFICAÇÃO INTELIGENTE (Espera até 5 segundos)
print("\nVerificando ficheiro no Desktop...")
sucesso = False
for tentativa in range(5):
    if os.path.exists(destino):
        sucesso = True
        break
    sleep(1.0)

# ── RESULTADO FINAL ─────────────────────────────────────────

print("═" * 60)
if sucesso:
    tamanho = os.path.getsize(destino) / 1024
    print(f"✅ SUCESSO: A tua arte foi guardada!")
    print(f"   Local: {destino}")
    print(f"   Tamanho: {tamanho:.1f} KB")
else:
    print(f"❌ ERRO: O ficheiro não foi encontrado.")
    print("   Possível causa: A janela 'Guardar Como' não aceitou o caminho.")
print("═" * 60)

print("\nParabéns — completaste todos os exercícios da Aula 04! 🎨")

# ── DESAFIO ────────────────────────────────────────────────
# Abre o ficheiro PNG guardado com o visualizador do Windows:
import subprocess
subprocess.Popen(['explorer', destino])