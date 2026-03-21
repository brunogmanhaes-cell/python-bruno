import os
os.system("cls")

id = int(input("Idade: "))
if id >= 18:
    print(f"Você tem {id}: Maior de Idade")
else:
    print(f"Você tem {id}: Menor de Idade")