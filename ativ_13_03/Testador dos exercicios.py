def exercic1():
    num = int(input("Digite um número para descobrir o quadrado dele: "))
    quad = num ** 2
    print(f"O quadrado de {num} é: {quad}")

def exercic2():
    num = int(input("Digite um número para dobrar seu valor: "))
    dobro= num * 2
    print(f"O dobro de {num} é: {dobro}")

def exercic3():
    print("Digite 4 números para descobrir sua média")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    num4 = float(input("Digite o quarto número: "))
    media = (num1 + num2 + num3 + num4) / 4
    print(f"A média total é {media}")
    print(f"A média aproximada é {media:.2f}")

def exercic4():
    num = int(input("Digite um número para descobrir o cubo dele: "))
    cubo = num ** 3
    print(f"O cubo de {num} é: {cubo}")

def exercic5():
    print("Descubra quantos Km/l o carro percorreu:")
    km = float(input("Digite os Km: "))
    litro = float(input("Digite os l: "))
    mediaKmL = km/litro
    print(f"Foi percorrido: {mediaKmL:.2f}")

def exercic6():
    print("Descubra quanto você gastou com cigarros:")
    preco = float(input("Digite o preço do cigarro: "))
    dias = int(input("Digite quantos maços fuma por dia: "))
    anos = float(input("Digite os anos fumando: "))
    anosR = anos * 365
    result = preco * dias * anosR
    print(f"Foi gasto aproximadamente: R${result:.2f}")

def exercic7():
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

def exercic8():
    num = int(input("Digite um número para descobrir o próximo número divisível por 5: "))
    resto = num % 5
    proximo = num + (5 - resto)
    print(f"O proximo número divisível por 5 é: {proximo}")

while True:
    import os
    os.system("cls")
    
    print("Bem vindo ao teste de exercicios do dia 13/03 de python\n"
    "Exercício 1 - Número ao quadrado\n"
    "Exercício 2 - Dobro do número\n"
    "Exercício 3 - Média de 4 números\n"
    "Exercício 4 - Número ao cubo\n"
    "Exercício 5 - Quilômetros por Litro\n"
    "Exercício 6 - Contador de gasto em cigarros\n"
    "Exercício 7 - Descobrir quantidade de cédulas necessárias\n"
    "Exercício 8 - Próximo numero divisível por 5\n")

    exerc = int(input("Selecione qual exercicio você quer testar: "))

    if exerc == 1:
        exercic1()
        
    elif exerc == 2:
        exercic2()

    elif exerc == 3:
        exercic3()

    elif exerc == 4:
        exercic4()

    elif exerc == 5:
        exercic5()

    elif exerc == 6:
        exercic6()

    elif exerc == 7:
        exercic7()

    elif exerc == 8:
        exercic8()
        
    else: 
        print("Exercíccio invalido")

    repetir = input("Quer testar outro exercício? (S/N)").lower()

    if repetir == "n" or repetir == "não" or repetir == "nao" or repetir == "no":
        print("Testador encerrado")
        break