import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota: "))
if 0 <= nota1 <=10:
    nota2 = float(input("Digite sua segunda nota: "))
    if 0 <= nota2 <=10:
        media = (nota1 + nota2)/2
        if media < 5:
            print(f"Sua nota é {media:.2f}: Reprovado")

        elif media >= 10:
            print(f"Sua nota é {media:.2f}: Aprovado com exelencia")

        else:
            print(f"Sua nota é {media:.2f}: Aprovado")
    else:
        print("Nota 2 inválida")

else:
    print("Nota 1 inválida")