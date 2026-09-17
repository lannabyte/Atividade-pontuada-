import os
os.system('cls')

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco = float(input("Digite o preço unitário: "))

total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_pagar = total - desconto

print("\nProduto:", nome)
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
