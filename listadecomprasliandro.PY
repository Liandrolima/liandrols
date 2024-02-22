from time import sleep

lista_de_compras = []

def adicionar_produto():
    nome_produto = str(input("Digite o nome do produto: "))

    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade de produtos no estoque: "))
            if quantidade_produto >= 1:
                break
            else:
                print("Digite um valor positivo")
        except ValueError:
                print("ERROR, digite um valor válido")
                
    while True:
        try:
            preco_produto = float(input("Digite o preço do produto:R$ "))
                        
            if preco_produto > 0:
                break
            else:
                print("Insira um valor válido")
        except ValueError:
                print("ERROR, digite um valor válido")
    preco_total_produto = quantidade_produto * preco_produto

    dicionario_produto = {
                "Nome": nome_produto,
                "Quantidade": quantidade_produto,
                "Preço": preco_produto,
                "Valor_total": preco_total_produto
                 }        
            
    lista_de_compras.append(dicionario_produto)

    print("Produto adicionado com sucesso")
    print("Valor total das compras até agora:", calcular_valor_total())

def calcular_valor_total():
    valor_total_lista = 0
    for produto in lista_de_compras:
        valor_total_lista += produto["Valor_total"]
    return valor_total_lista

def visualizar_produtos():
    for i ,produto in enumerate(lista_de_compras):
        print(f"{i} - {produto}")
    print("Valor total das compras até agora:", calcular_valor_total())

def deletar_produto():
            visualizar_produtos()
            try:
                posicao_excluida = int(input("Digite o número do produto que você quer deletar: "))
                if posicao_excluida >= 0 and posicao_excluida < len(lista_de_compras):
                    lista_de_compras.pop(posicao_excluida)
                    sleep(1,5)
                    return "Produto excluído com sucesso"
                else:
                    return "Meu fiiiii, digite uma posição dentro da lista que eu mostrei"
            except ValueError:
                 print("ERROR, digite um valor válido")
                 

def editar_produto():
    visualizar_produtos()
    try:
        posicao_editar = int(input("Digite o número do produto que você quer editar: "))
        if posicao_editar >= 0 and posicao_editar < len(lista_de_compras):
            submenu = int(input("""
            Escolha uma opção:
            1 - Atualizar Nome do produto
            2 - Atualizar Quantidade do estoque do produto
            3 - Atualizar Preço do produto
"""))   
            match submenu:
                case 1:
                    nome_produto = str(input("Digite o novo nome do produto: "))
                    lista_de_compras[posicao_editar]["Nome"] = nome_produto
                case 2:
                    while True:
                        try:
                            print(f"Quantidade atual: {lista_de_compras[posicao_editar]["Quantidade"]}")
                            quantidade_produto = int(input("Digite a nova quantidade do produtos no estoque: "))
                            if quantidade_produto >= 1:
                                lista_de_compras[posicao_editar]["Quantidade"] = quantidade_produto
                                break
                            else:
                                print("Digite um valor positivo")
                        except ValueError:
                            print("ERROR, digite um valor válido")
                case 3:
                      while True:
                        try:
                            preco_produto = float(input("Digite o novo preço do produto:R$ "))

                            if preco_produto > 0:
                                lista_de_compras[posicao_editar]["Preço"] = preco_produto
                                break
                            else:
                                print("Insira um valor válido")
                        except ValueError:
                            print("ERROR, digite um valor válido")
                    
            return "Produto excluído com sucesso"
        else:
            return "Meu fiiiii, digite uma posição dentro da lista que eu mostrei"
    except ValueError:
                 print("ERROR, digite um valor válido")

def teleInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
            return 0
        else:
            return n
        
def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    sleep(1)
    cabeçalho('          \033[30;42mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = teleInt('\033[36mSua opção: \033[m')
    return opc
                 
from os import system

while True:
    try:
        resposta = menu(['Adicionar Produto', 'Excluir Produto', 'Ver a lista de Produtos', 'Atualizar Produto', 'Sair do sistema'])
        
        system("cls")
        match resposta:
            case 1:
                adicionar_produto()
            case 2:
                print(deletar_produto())
            case 3:
                visualizar_produtos()
            case 4:
                  editar_produto()
            case 5:
                print("Fim do programa")
                break
            case _:
                print("Opção inválida")
    except ValueError:
         print(f"ERROR: Digite um valor válido")
    sleep(1.5)
