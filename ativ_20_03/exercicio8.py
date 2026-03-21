import os
os.system("cls")

nota = float(input("Digite sua nota: "))

if 0 <= nota <=10:
    print(f"Sua nota é {nota}: Válida")

else:
    print(f"Sua nota é {nota}: Inválida")
    