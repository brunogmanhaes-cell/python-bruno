import os
os.system("cls")

n1 = float(input("Digite sei primeiro numero: "))
n2 = float(input("Digite seu segundo numero: "))
n3 = float(input("Digite seu terceiro numero: "))

if n1 > n2:
    if n1 < n3:
        print(f"O numero intermediario é {n1}")

elif n1 > n3:
    if n1 < n2:
        print(f"O numero intermediario é {n1}")

elif n2 > n3:
    if n2 < n1:
        print(f"O numero intermediario é {n2}")

elif n2 > n1:
    if n2 < n3:
        print(f"O numero intermediario é {n2}")

elif n3 > n1:
    if n3 < n2:
        print(f"O numero intermediario é {n3}")

elif n3 > n2:
    if n3 < n1:
        print(f"O numero intermediario é {n3}")

else:
    print("Eles tem o mesmo valor")
    