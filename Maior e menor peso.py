pesado = 0
leve = 0

for medidor in range(1,6):
    peso = float(input(f'\nEntre com o {medidor}º peso:'))

    print(f'\nO peso introdozido foi: {peso:.2f}kg')
    if medidor == 1:
        pesado = leve = peso
    if peso > pesado:
        pesado = peso
    if peso < leve:
        leve = peso
print()
print(f'O número maior é: {pesado:.2f}')
print(f'O número menor é: {leve:.2f}')
input('\nEnter para terminar')