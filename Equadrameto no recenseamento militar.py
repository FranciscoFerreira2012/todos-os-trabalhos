from datetime import date

def RecenseamentoMilitar():
    ano = date.today().year
    anoDeNascimento = int(input('Qual foi o ano em que tu nasceste?'))
    if anoDeNascimento > 2007:
        print('Já passou o prazo para o recenseamento.')
    elif anoDeNascimento == 2007:
        print('Está no momento de recenseamento.')
    elif anoDeNascimento < 2007:
        print('Ainda não tens idade para o recenseamento.')

RecenseamentoMilitar()