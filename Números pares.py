começo= int(input('Entre com o primeiro número: '))
final = int(input('Entre com o segundo número: '))
escolha = int(input('1 - Par \n2 - Impar \nEsclha a opção: '))
print()

if escolha == 1:
    print('Os números pares são:')
    print()
elif escolha == 2:
    print('Os números impares são:')
    print()

for x in range (começo, final +1):
    if x % 2 ==0:
        if x % 2 == 0:
            print(x, end=' ')
    elif escolha == 2:
        if x % 2 == 1:
            print(x, end=' ')
    else:
        print('Opção inválida')
        break

print()
print('FIM')