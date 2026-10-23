import pyautogui
from time import sleep

pyautogui.FAILSAFE = True

largura, altura = pyautogui.size()
print(f'Resolução do ecrã: {largura} x {altura} px')
print('A iniciar em 3 segundos... (move o rato para (0,0) para parar)\n')
sleep(3)

print('Canto superior esquerdo...')
pyautogui.moveTo(50, 50, duration=1)
sleep(0.5)

print('Canto superior direito...')
pyautogui.moveTo(largura - 50, 50, duration=1)
sleep(0.5)

print('Canto inferior direito...')
pyautogui.moveTo(largura - 50, altura - 50, duration=1)
sleep(0.5)

print('Canto inferior esquerdo...')
pyautogui.moveTo(50, altura - 50, duration=1)
sleep(0.5)

print('Meio...')
pyautogui.moveTo(largura // 2, altura // 2, duration=1)

print('\nConcluído!')