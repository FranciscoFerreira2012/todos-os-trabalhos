Países = ["Alemanha", "Portugal", "Vaticano", "Rússia", "Ucrania", "Suécia", "Irlanda", "Islândia", "Vaticano", "Reino Unido", "Espanha", "San Marino", "França", "Bélgica", "Países Baixos", "Luxemburgo", "Suíça", "Bielorússia", "Noruega", "Finlândia",]
while True:
    escolha = str(input('Escolhe um país NA EUROPA!!!!!  '))
    if escolha in Países:
        print ('\nBoa, escolheste um país na Europa.')
        break
    else:
        print('\nAs letras em maiúsculo nao era o suficiente?')
        break