def verificar_numero():
    # Solicita ao usuário que insira um número
    numero = float(input("Digite um número: "))

    # Verifica se o número é positivo, negativo ou zero
    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print("O número é zero.")

# Chama a função para executar o programa
verificar_numero()
