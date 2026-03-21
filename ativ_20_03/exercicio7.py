import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2
if media < 5:
    print(f"Sua nota é {media:.2f}: Reprovado")

elif media >= 10:
    print(f"Sua nota é {media:.2f}: Aprovado com exelencia")

else:
    print(f"Sua nota é {media:.2f}: Aprovado")
    