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
    

if ladoA == ladoB == ladoC:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo Equilátero.")

elif ladoA == ladoB:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo Isosceles.")

elif ladoA == ladoC:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo Isosceles.")

elif ladoB == ladoC:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo Isosceles.")

else:
    print(f"Os lados {ladoA}, {ladoB} e {ladoC} formam um triângulo Escaleno.")