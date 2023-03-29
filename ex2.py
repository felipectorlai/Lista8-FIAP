# Obter o primeiro número do usuário
num1 = int(input("Digite o primeiro número: "))

# Obter o segundo número do usuário
num2 = int(input("Digite o segundo número: "))

# Percorrer todos os números entre num1 e num2 (exclusivo)
for i in range(num1 + 1, num2):
    print(i, end=" ") 

