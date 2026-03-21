import os
os.system("cls")

sal = float(input("Salário: "))

if sal <= 2259.20:
    ir = sal * 0

elif 2259.21 <= sal <= 2826.65:
    ir = sal * 0.075 - 169.24

elif 2826.66 <= sal <= 3751.05:
    ir = sal * 0.15 - 381.44

elif 3751.06 <= sal <= 4664.68:
    ir = sal * 0.225 - 662.77

else:
    ir = sal * 0.275 - 896

print(f"Salário: R$ {sal}")
print(f"IR: R$ {ir:.2f}")