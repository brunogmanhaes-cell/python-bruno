import os
os.system("cls")

print("Digite 4 números para descobrir sua média")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media = (num1 + num2 + num3 + num4) / 4

print(f"A média total é {media}")
print(f"A média aproximada é {media:.2f}")