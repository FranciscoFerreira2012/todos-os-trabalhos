velocidade = int(input("Qual é a sua velocidade?"))
if velocidade>120:
    velocidadeExcesso = (velocidade-120)*4
    mensagem = "Estás muito acima do limite permitido. A multa foi gerada no valor de {} euros".format(velocidadeExcesso)
elif velocidade>80:
    velocidadeExcesso = (velocidade-80)*2
    mensagem = "Estás acima do limite permitido. A multa foi gerada no valor de {} euros".format(velocidadeExcesso)
else:
    mensagem = "Está dentro do limite. Boa viagem!"
print(mensagem)
