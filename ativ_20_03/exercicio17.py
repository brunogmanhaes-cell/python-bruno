import os
os.system("cls")

ladoA = int(input("Valor do lado A:"))
ladoB = int(input("Valor do lado B:"))
ladoC = int(input("Valor do lado C:"))
print(f"Lado A: {ladoA}")
print(f"Lado B: {ladoB}")
print(f"Lado C: {ladoC}")

somaAB = ladoA + ladoB

if somaAB < ladoC:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} não formam um triângulo.")


else:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo.")
    
