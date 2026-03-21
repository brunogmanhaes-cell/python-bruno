import os
os.system("cls")

compra = float(input("Digite o valor da sua compra:"))
print("Digite sua forma de pagamento\n"
"1 - PIX (desconto de 5%)\n"
"2 - Dinheiro (O mesmo valor da compra)\n"
"3 - Débito (Acréscimo de 1%)\n"
"4 - Crédito (Acréscimo de 2,5%)")
pagma = int(input())
if pagma == 1:
    reajuste = compra - (compra * 0.05)

elif pagma == 2:
    reajuste = compra

elif pagma == 3:
    reajuste = compra + (compra * 0.01)

elif pagma == 4:
    reajuste = compra + (compra * 0.025)

print(f"Valor original: {compra}\n"
  f"Valor ajustado: {reajuste}")