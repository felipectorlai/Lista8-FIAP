
maior = None
menor = None

while True:
    numero = int(input("Digite um número inteiro positivo (digite um número menor ou igual a 0 para sair): "))

    if numero <= 0:
        break

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

if maior is not None:
    print("O maior número digitado foi:", maior)

if menor is not None:
    print("O menor número digitado foi:", menor)