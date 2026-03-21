import os
os.system("cls")

valor = float(input("Valor: "))
if valor < 5000:
    desconto = valor - (valor * 0.035)
    print(f"Sua compra de {valor} ganhou um desconto de 3,5% e foi para: {desconto:.2f}")

else:
    desconto = valor - (valor * 0.075)

print(f"Sua compra de {valor} ganhou um desconto de 7,5% e foi para: {desconto:.2f}")