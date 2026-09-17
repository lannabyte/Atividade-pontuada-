import os
os.system('cls')

renda_mensal = float(input("Digite a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: R$ "))
num_parcelas = int(input("Digite o número de prestações desejado: "))

valor_prestacao = valor_emprestimo / num_parcelas
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

emprestimo_valido = valor_emprestimo <= limite_emprestimo
prestacao_valida = valor_prestacao <= limite_prestacao

print("\n--- Análise de Crédito ---")
print(f"Valor da prestação: R$ {valor_prestacao:.2f}")
print(f"Limite máximo da prestação (30%): R$ {limite_prestacao:.2f}")
print(f"Limite máximo do empréstimo (10x renda): R$ {limite_emprestimo:.2f}")

if emprestimo_valido and prestacao_valida:
    print("\nResultado: Empréstimo CONCEDIDO!")
else:
    print("\nResultado: Empréstimo NEGADO.")
    if not emprestimo_valido:
        print("- Motivo: O valor total solicitado excede 10 vezes a renda mensal.")
    if not prestacao_valida:
        print("- Motivo: O valor da prestação ultrapassa 30% da renda mensal.")