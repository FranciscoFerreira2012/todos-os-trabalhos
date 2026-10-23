# ── IMPORTAÇÃO DE BIBLIOTECAS ────────────────────────────────
import pyautogui    # Controla o rato e o teclado (o nosso "robô")
import math         # Fornece funções matemáticas (Seno, Cosseno, Radianos)
from time import sleep # Permite fazer pausas para o Windows processar as ações

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 04C — Desenhar Círculo e Triângulo (Versão Final)
# ═══════════════════════════════════════════════════════════

# Segurança: se o utilizador puxar o rato para o canto do ecrã, o script para.
pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
LADO   = 200  # Tamanho do quadrado que já existe no Paint
RAIO   = 80   # Raio do círculo e metade da base/altura do triângulo
PASSOS = 60   # Resolução original (mantida por compatibilidade, modificamos para PASSOS_EXTENDED, pois o paint pode não desenhar tudo)
# ────────────────────────────────────────────────────────────

# Usamos o nosso truque de multiplicação de strings para o menu
print("═" * 60)
print("🪄 O ASSISTENTE VAI COMEÇAR!")
print("Abre o Paint onde tens o quadrado pintado.")
print("═" * 60 + "\n")
sleep(2)

# ── 1. FASE DE CAPTURA (O robô aprende onde clicar) ──────────

# PASSO 1: O robô precisa de saber onde está a ferramenta Pincel
print("🖌️ PASSO 1: Põe o rato no botão do PINCEL (não cliques!)")
for i in range(5, 0, -1):
    print(f"  A gravar em {i}...")
    sleep(1.0)
X_PINCEL, Y_PINCEL = pyautogui.position() # Guarda a coordenada do Pincel
print(f"✓ Pincel guardado!\n")

# PASSO 2: O robô precisa de uma referência no ecrã (o quadrado anterior)
print("🔲 PASSO 2: Põe o rato no CANTO SUPERIOR ESQUERDO do quadrado")
for i in range(5, 0, -1):
    print(f"  A gravar em {i}...")
    sleep(1.0)
X_INICIO, Y_INICIO = pyautogui.position() # Guarda a coordenada de início
print(f"✓ Posição do quadrado guardada!\n")

print("Tudo pronto! Podes largar o rato. A automação vai começar...\n")
sleep(1)

# ── 2. FASE DE AUTOMAÇÃO (O robô executa o desenho) ──────────

# Focar o Paint: um clique inicial garante que a janela está ativa
pyautogui.click(X_INICIO, Y_INICIO)
sleep(0.3)

# Selecionar o Pincel: clica no botão que capturámos antes
print("A trocar para o Pincel...")
pyautogui.click(X_PINCEL, Y_PINCEL)
sleep(0.5)

# ── CÍRCULO (Usando Trigonometria) ──────────────────────────
print("Passo 1: A desenhar círculo (com dragTo!)...")

# Definir o centro do círculo (cx, cy) à direita do quadrado
cx = X_INICIO + LADO + 150
cy = Y_INICIO + LADO // 2

# Aumentamos os passos para 100 para a curva ficar mais suave
PASSOS_EXTENDED = 100

# Calcular o Ponto de Partida (Grau 0)
# Fórmula: Centro + Raio * Cosseno/Seno (convertido para radianos)
px0 = cx + int(RAIO * math.cos(math.radians(0)))
py0 = cy + int(RAIO * math.sin(math.radians(0)))

# Mover para o início sem riscar
pyautogui.moveTo(px0, py0)

# Ciclo para desenhar a curva ponto a ponto
# Adicionamos +5 no range para ele "atropelar" o início e fechar bem o círculo
for i in range(1, PASSOS_EXTENDED + 5):
    angulo = (360 / PASSOS_EXTENDED) * i
    px = cx + int(RAIO * math.cos(math.radians(angulo)))
    py = cy + int(RAIO * math.sin(math.radians(angulo)))

    # No Windows 11, usamos dragTo para garantir que o traço aparece
    pyautogui.dragTo(px, py, button='left')

# Forçar o fecho final no ponto zero exato para evitar buracos de arredondamento
pyautogui.dragTo(px0, py0, button='left')
sleep(0.7)

# ── TRIÂNGULO (Usando Geometria de Vértices) ────────────────
print("Passo 2: A desenhar triângulo...")

# Puxar o triângulo para DEBAIXO do quadrado (evita desenhar fora da folha)
tx = X_INICIO + LADO // 2     # Centro horizontal alinhado com o quadrado
ty = Y_INICIO + LADO + 120    # Posicionado 120px abaixo do quadrado

# Definir os 3 pontos (vértices)
v1 = (tx,          ty - RAIO)         # Vértice Superior (Topo)
v2 = (tx - RAIO,   ty + RAIO)         # Vértice Inferior Esquerdo
v3 = (tx + RAIO,   ty + RAIO)         # Vértice Inferior Direito

# Desenhar o triângulo com arrastamento contínuo (dragTo)
pyautogui.moveTo(v1[0], v1[1]) # Posicionar no topo
pyautogui.dragTo(v2[0], v2[1], duration=0.6, button='left') # Riscar até à esquerda
pyautogui.dragTo(v3[0], v3[1], duration=0.6, button='left') # Riscar até à direita
pyautogui.dragTo(v1[0], v1[1], duration=0.6, button='left') # Fechar no topo

print("\n✓ Círculo e triângulo desenhados!")
print("Próximo: ex04d para guardar a arte como PNG no Desktop.")

# ── DESAFIO: Estrela de 5 Pontas ──────────────────────────────
print("Passo 3: A desenhar Estrela de 5 pontas...")

# Posicionar a estrela à direita do círculo
ex = cx + RAIO * 2 + 100 
ey = cy

# Uma estrela de 5 pontas tem 10 vértices (5 pontas + 5 centros)
pontos = 10 

# Mover para o primeiro ponto antes de começar
angulo_rad = math.radians(-90) # Começar no topo (-90 graus)
px0 = ex + int(RAIO * math.cos(angulo_rad))
py0 = ey + int(RAIO * math.sin(angulo_rad))
pyautogui.moveTo(px0, py0)

# Ciclo para desenhar as 10 linhas da estrela
for i in range(1, pontos + 1):
    # Ângulo de cada vértice (360 graus / 10 pontos = 36 graus por passo)
    angulo = math.radians(i * (360 / pontos) - 90)
    
    # Alternar entre Raio total (ponta) e Metade do Raio (centro)
    r = RAIO if i % 2 == 0 else RAIO // 2
    
    px = ex + int(r * math.cos(angulo))
    py = ey + int(r * math.sin(angulo))
    
    # Desenhar com o nosso dragTo de confiança
    pyautogui.dragTo(px, py, duration=0.4, button='left')

print("✓ Estrela desenhada com sucesso!")