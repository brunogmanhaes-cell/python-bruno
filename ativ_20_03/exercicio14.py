import os
os.system("cls")

n1 = float(input("Digite sei primeiro numero: "))
n2 = float(input("Digite seu segundo numero: "))
n3 = float(input("Digite seu terceiro numero: "))

if n3 < n1 > n2:
    print(f"O maior número é {n1}")

elif n1 < n2 > n3:
    print(f"O maior número é {n2}")

elif n1 < n3 > n2:
    print(f"O maior número é {n3}")
    
else:
    print("Eles tem o mesmo valor")
    