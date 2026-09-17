import os
os.system('cls')

cor = input("Digite a cor do CD: ").lower()

if cor == "verde":
    preco = 10

elif cor == "azul":
    preco = 20

elif cor == "amarelo":
    preco = 30

elif cor == "vermelho":
    preco = 40

else:
    preco = 0
    print("Cor inválida")

if preco != 0:
    print("Preço: R$", preco)