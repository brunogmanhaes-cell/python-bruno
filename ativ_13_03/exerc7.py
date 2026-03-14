import os
os.system("cls")

valor = int(input("Digite o valor (múltiplo de 10): "))

ced50 = valor // 50
valor1 = valor % 50

ced20 = valor1 // 20
valor2 = valor1 % 20

ced10 = valor2 // 10

print("Cédulas necessárias:")
print("50 reais:", ced50)
print("20 reais:", ced20)
print("10 reais:", ced10)
