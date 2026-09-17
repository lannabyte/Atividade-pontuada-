import os
os.system('cls')

operacao = input("Digite a operação (+, -, * ou /): ")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    resultado = A / B
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
