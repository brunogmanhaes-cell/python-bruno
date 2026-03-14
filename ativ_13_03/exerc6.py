import os
os.system("cls")

print("Descubra quanto você gastou com cigarros:")

preco = float(input("Digite o preço do cigarro: "))
dias = int(input("Digite quantos maços fuma por dia: "))
anos = float(input("Digite os anos fumando: "))

anosR = anos * 365
result = preco * dias * anosR

print(f"Foi gasto aproximadamente: R${result:.2f}")