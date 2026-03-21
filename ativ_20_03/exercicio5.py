import os
os.system("cls")

num = int(input("Digite um número: "))

resto = num % 5

if resto == 0:
    print(f"{num} já é múltiplo de 5")

else:
    resto2 = num + (5 - resto)
    print(f"Próximo múltiplo é: {resto2}")
