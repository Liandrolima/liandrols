estoque = []

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Fruta
    2 - Excluir Fruta
    3 - Ver todas as Frutas
    0 - Sair do menu
"""))
    match menu:
        case 1:
            fruta_adicionada = str(input("Digite uma fruta: "))
            estoque.append(fruta_adicionada)
            print("Fruta adicionada com sucesso")
        case 2:
            for fruta in estoque:
                print(fruta)
            fruta_excluida = str(input("Digite o nome da fruta que você quer deletar: "))
            if fruta_excluida in estoque:
                posicao_do_excluido = estoque.index(fruta_excluida)
                estoque.pop(posicao_do_excluido)
            print("Fruta excluída com sucesso")
        case 3:
            for i ,fruta in enumerate(estoque):
                print(f"{i+1} - {fruta}")
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")