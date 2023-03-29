
taxa_abatimento = float(input("Digite a taxa de abatimento em porcentagem: "))
num_prestacoes = int(input("Digite o número de prestações: "))
valor_prestacao = float(input("Digite o valor da primeira prestação: "))

for i in range(num_prestacoes):
    print(f"Prestação {i + 1}: R$ {valor_prestacao:.2f}")
    valor_prestacao *= 1 - taxa_abatimento / 100