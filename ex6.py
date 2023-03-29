
senha_correta = 1234  # Definindo a senha correta

while True:  # Repete até que a senha seja correta
    senha_digitada = int(input("Digite a senha numérica: "))

    if senha_digitada == senha_correta:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")