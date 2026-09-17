import os
os.system('cls')

combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ")
litros = float(input("Digite a quantidade de litros: "))

if combustivel == "A" or combustivel == "a":
    preco = 3.79

    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20

elif combustivel == "G" or combustivel == "g":
    preco = 6.59

    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30

else:
    print("Combustível inválido")
    preco = 0
    desconto = 0

total = litros * preco
valor_desconto = total * desconto
valor_pagar = total - valor_desconto

if preco != 0:
    print("Valor a pagar: R$", valor_pagar)

