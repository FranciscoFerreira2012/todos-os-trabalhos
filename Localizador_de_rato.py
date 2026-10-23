import pyautogui
from time import sleep

print('=' * 50)
print('      LOCALIZADOR DE COORDENADAS - PyAutoGui')
print('=' * 50)
print('Posiciona o rato e prie ENTER para ver as coordenadas.')
print('Prima CTRL+C para sair.\n')

try:
    while True:
        input('Prima ENTER... ')
        pos = pyautogui.position()
        print(f'  >> Coordenadas: X={pos.x}  Y={pos.y}\n')
except KeyboardInterrupt:
    print('\nPrograma terminado.')

