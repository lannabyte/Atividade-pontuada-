import os
os.system('cls')

A = int(input('Digite A: '))
B = int(input('Digite B: '))
C = int(input('Digite C: '))

soma = A + B

if soma < C:
    print("A soma de A + B é menor que C")
elif soma > C:
    print("A soma de A + B é maior que C")
else:
    print("A soma de A + B é igual a C")