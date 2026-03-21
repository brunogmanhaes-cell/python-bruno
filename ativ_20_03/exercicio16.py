import os
os.system("cls")

n1 = float(input("Digite seu primeiro numero: "))
n2 = float(input("Digite seu segundo numero: "))
n3 = float(input("Digite seu terceiro numero: "))

if n1 <= n2:
    if n1 <= n3:
        if n3 >= n2:
            print(f"Ordem crescente: {n1}, {n2} e {n3}")
        elif n3 <= n2:
            print(f"Ordem crescente: {n1}, {n3} e {n2}")


elif n2 <= n1:
    if n2 <= n3:
        if n3 >= n1:
            print(f"Ordem crescente: {n2}, {n1} e {n3}")
        elif n3 < n1:
            print(f"Ordem crescente: {n2}, {n3} e {n1}")

elif n3 <= n1:
    if n3 <= n2:
        if n2 >= n1:
            print(f"Ordem crescente: {n3}, {n1} e {n2}")
        elif n2 <= n1:
            print(f"Ordem crescente: {n3}, {n2} e {n1}")


    