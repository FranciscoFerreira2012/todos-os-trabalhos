nota = int(input("Qual é a nota? "))
match nota:
    case 20:
        avaliação = "Excelente"
    case 18:
        avaliação = "Muito bom"
    case _:
        avaliação = "Nota não reconhecida"
print(avaliação)