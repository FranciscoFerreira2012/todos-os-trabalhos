primeiro_número = int(input('Qual é o primeiro número?'))
último_número = int(input('Qual é o último número?'))
soma = 0

print('\nOs valores somados são:')
for valor in range(primeiro_número, último_número + 1):
    soma += valor
    if valor == primeiro_número:
        print(f'[ {valor}', end= ' + ')
    elif valor == último_número:
        print(valor, end=' + ')
    else:
        print(valor, end=' + ')

print()
print(f'\nA soma de todos os números de {primeiro_número} até {último_número} é {soma}\n')
