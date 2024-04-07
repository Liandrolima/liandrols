import random

def jogo_de_adivinhacao():
    # Gerar um número aleatório entre 1 e 10
    numero_aleatorio = random.randint(1, 10)
    
    tentativas = 0
    max_tentativas = 3
    
    while tentativas < max_tentativas:
        # Solicitar ao jogador que adivinhe o número
        tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
        
        # Incrementar o número de tentativas
        tentativas += 1
        
        # Verificar se a tentativa do jogador está correta
        if tentativa == numero_aleatorio:
            print("Parabéns! Você acertou!")
            break
        else:
            print("Tente novamente!")
    else:
        print(f"Suas {max_tentativas} tentativas acabaram. O número correto era {numero_aleatorio}.")

# Chamar a função para iniciar o jogo
jogo_de_adivinhacao()
