import os
os.system("cls")

sal = float(input("Salário: "))

if sal <= 1518:
    inss = sal * 0.075

elif 1518.01 <= sal <= 2793.88:
    inss = sal * 0.09 - 22.77

elif 2793.89 <= sal <= 4190.83:
    inss = sal * 0.12 - 106.59

else:
    inss = sal * 0.14 - 190.40

print(f"Salário: R$ {sal}")
print(f"INSS: R$ {inss:.2f}")