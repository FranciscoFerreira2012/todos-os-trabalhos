
def Cabecalho(texto):
    print()
    cumprimento = len(texto) + 6
    print('='*cumprimento + 2)
    str(print(f'|| {texto} ||'))
    print('='*cumprimento)
    print()


def Menu():
    Cabecalho('Jogo do Galo')


Menu()