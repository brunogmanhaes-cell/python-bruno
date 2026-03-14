import os
os.system("cls")

print("Descubra quantos Km/l o carro percorreu:")
km = float(input("Digite os Km: "))
litro = float(input("Digite os l: "))
mediaKmL = km/litro
print(f"Foi percorrido: {mediaKmL:.2f}")