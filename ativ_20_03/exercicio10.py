import os
os.system("cls")

valor = float(input("Valor: "))
if valor <= 100:
    desconto = valor * 0.95
    print(f"Sua compra de {valor} ganhou um desconto de 5% e foi para: {desconto:.2f}")
else:
    desconto = valor * 0.90

print(f"Sua compra de {valor} ganhou um desconto de 10% e foi para: {desconto:.2f}")