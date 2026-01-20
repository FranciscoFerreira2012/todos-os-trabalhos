ordenado = float(input("Qual é o seu ordenado atual?"))
if ordenado < 500:
   reajuste = 15
elif ordenado <= 1000:
   reajuste = 10
else:
   reajuste = 5
valor_aumento = (ordenado * reajuste) / 100

novo_salario = ordenado + valor_aumento

print(f"\nO reajuste será de {reajuste}%")
print(f"O aumento será de {valor_aumento:.2f}€")
print(f"O novo salário passará para {novo_salario:.2f}€")
