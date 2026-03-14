import os
os.system("cls")

num = int(input("Digite um número para descobrir o proximo número divisivel por 5: "))

resto = num % 5
proximo = num + (5 - resto)

print(f"O proximo número divisivel por 5 é: {proximo}")