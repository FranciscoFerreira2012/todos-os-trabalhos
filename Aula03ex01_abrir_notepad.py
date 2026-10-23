# Aula03ex01_abrir_notepad.py

import os
import pyautogui
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 03A — Versão Original (Apenas aula03.txt)
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

frase1 = input('Qual é a primeira frase que deseja escrever? ')
frase2 = input('Qual é a segunda frase que deseja escrever? ')
frase3 = input('Qual é a terceira frase que deseja escrever? ')

print("A iniciar em 3 segundos...")
print(">> MINIMIZA o Visual Studio agora! <<\n")
sleep(3)

# Passo 1 — Abrir Bloco de Notas com Win+R
print("Passo 1: A abrir Bloco de Notas...")
pyautogui.hotkey('win', 'r')
sleep(0.8)
pyautogui.write('notepad', interval=0.05)
pyautogui.press('enter')
sleep(1.5)

# Passo 2 — Escrever as 3 linhas
print("Passo 2: A escrever texto...")
linhas = [
    frase1,
    frase2,
    frase3,
]
for linha in linhas:
    pyautogui.write(linha, interval=0.05)
    pyautogui.press('enter')
    sleep(0.2)

# Passo 3 — Guardar APENAS como aula03.txt
print("Passo 3: A pedir para Guardar Como...")

#WINDOWS 11 - USAR A LINHA ABAIXO
pyautogui.hotkey('ctrl', 'shift', 'd') # O atalho da tua fotografia

#WINDOWS 10 - USAR A LINHA ABAIXO
pyautogui.hotkey('ctrl', 'shift', 's') # O atalho "Guardar como"

sleep(2.0)

print("A escrever o nome aula03.txt...")
pyautogui.write('aula03.txt', interval=0.05)
sleep(0.5)
pyautogui.press('enter')
sleep(1.0)

# ── PROTEÇÃO "FICHEIRO JÁ EXISTE" ────────────────────────
# Se já lá estiver um aula03.txt de testes anteriores, o Windows
# vai perguntar se queres substituir. Estas 2 linhas dizem "Sim".
pyautogui.press('left')
sleep(0.2)
pyautogui.press('enter')
sleep(1.5)
# ─────────────────────────────────────────────────────────

# Passo 4 — Fechar
print("Passo 4: A fechar...")
os.system("taskkill /f /im notepad.exe")

print("\n✓ SUCESSO! O ficheiro aula03.txt foi guardado!")
print("Próximo: ex03b para adicionar texto com acentos.")

# ── DESAFIO ────────────────────────────────────────────────
# Pede 3 frases ao utilizador ANTES do sleep(3):
#   f1 = input("Frase 1: ")
#   f2 = input("Frase 2: ")
#   f3 = input("Frase 3: ")
# Depois escreve-as no Bloco de Notas.