# Solicita dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Inicializa as variáveis de contagem
pares = 0
impares = 0

# Percorre os números entre num1 e num2
for num in range(num1, num2 + 1):
    # Verifica se o número é par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Imprime os resultados
print(f"Entre {num1} e {num2} há {pares} números pares e {impares} números ímpares.")