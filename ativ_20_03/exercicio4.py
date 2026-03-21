import os
os.system("cls")

id = int(input("Número: "))
numero = id % 2

if numero == 0:
    print("Número par")

else:
    print("Número impar")