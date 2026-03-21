import os
os.system("cls")

n1 = float(input("Digite sei primeiro numero: "))
n2 = float(input("Digite seu segundo numero: "))

if n1 > n2:
    print(f"O maior número é {n1}")

elif n2 > n1:
    print(f"O maior número é {n2}")

else:
    print("Eles tem o mesmo valor")
    