import os
os.system('cls')

kg_morango = float(input("Digite a quantidade de morangos: "))
kg_maca = float(input("Digite a quantidade de maçãs: "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total_kg = kg_morango + kg_maca
valor_total = preco_morango + preco_maca

if total_kg >= 10 or valor_total > 15:

    desconto = valor_total * 0.10

    valor_pagar = valor_total - desconto

else:

    valor_pagar = valor_total

print("Valor a pagar: R$", valor_pagar)