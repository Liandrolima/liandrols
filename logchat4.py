def calcular_soma_pares():
    # Solicita ao usuário que insira os números de início e fim do intervalo
    inicio = int(input("Digite o número de início do intervalo: "))
    fim = int(input("Digite o número de fim do intervalo: "))
    
    soma = 0
    # Loop for para iterar sobre todos os números no intervalo
    for numero in range(inicio, fim + 1):
        # Verifica se o número é par
        if numero % 2 == 0:
            soma += numero  # Adiciona o número par à soma
    
    # Verifica se houve algum número par no intervalo
    if soma == 0:
        print("Não há números pares no intervalo fornecido.")
    else:
        print(f"A soma dos números pares no intervalo [{inicio}, {fim}] é: {soma}")

# Chama a função para calcular a soma dos números pares
calcular_soma_pares()
