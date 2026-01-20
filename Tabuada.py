numero = int(input('\nEntre com o número desejado: '))
print()

print(f'** Tabuada do {numero} **')
print()

for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')

print()
print("Enter para Terminar")