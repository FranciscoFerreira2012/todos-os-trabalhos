with open('FicheiroUmaLinha.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('O Rodrigo é Cigano e Preto!')

with open('FicheiroTresLinhas.txt', 'w', encoding='utf-8') as ficheiro:
    ficheiro.write('Primeira linha de informação\n')
    ficheiro.write('Segunda linha de informação\n')
    ficheiro.write('Terceira linha de informação')

with open('FicheiroTresLinhas.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nLinha 4')

with open('FicheiroTresLinhas.txt', 'a', encoding='utf-8') as arquivo:
    novasLinhas = ['\nLinha 5', '\nLinha 6']
    arquivo.writelines(novasLinhas)

with open('FicheiroTresLinhas.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('FicheiroTresLinhas.txt', 'r', encoding='utf-8') as arquivo:
    linha1 = arquivo.readline()
    print(linha1)