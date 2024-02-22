from time import sleep
class Livro:
    def __init__(self, título, autor, ID, descricao, emprestado=False):
        self._título = título  
        self._autor = autor  
        self._ID = ID
        self.descricao = descricao
        self.emprestado = emprestado
    
    def get_título(self):
        return self._título
    
    def get_autor(self):
        return self._autor
    
    def get_ID(self):
        return self._ID
    
    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"Livro: {self._título} | Autor: {self._autor} | ID: {self._ID} | Descrição: {self.descricao} | Status: {status}"
    
class Membro:
    def __init__(self, nome, quantidade_de_membros, histórico_de_livros_emprestados):
        self._nome = nome  
        self._quantidade_de_membros = quantidade_de_membros  
        self._histórico_de_livros_emprestados = histórico_de_livros_emprestados
        
    def get_nome(self):
        return self._nome
    
    def get_quantidade_de_membros(self):
        return self._quantidade_de_membros
    
    def get_histórico_de_livros_emprestados(self):
        return self._histórico_de_livros_emprestados
    
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catálogo_de_livros = []
        self.membros = []
    
    def adicionar_livros(self, livro):
        self.catálogo_de_livros.append(livro)
        
    def listar_livros(self):
        print(f"\033[0;32mLivros da Biblioteca {self.nome}:\033[m")
        for livro, v in enumerate(self.catálogo_de_livros):
            print(livro, v)
    
    def remover_livros(self):
        print(f"\033[0;34mREMOVER LIVRO\033[m")
        while True:
            for livro, v in enumerate(self.catálogo_de_livros):
                print(livro, v)
            try:
                posicao_excluida = int(input("Digite o número do livro que você quer deletar: "))
                if posicao_excluida >= 0 and posicao_excluida < len(self.catálogo_de_livros):
                    self.catálogo_de_livros.pop(posicao_excluida)
                    print( "Livro excluído com sucesso")
                    break
                else:
                    return "Meu fiiiii, digite uma posição dentro da lista que eu mostrei"
            except (ValueError, TypeError):
                print(f'\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
                continue
            except (KeyboardInterrupt):
                print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
                return 0
            
    
    def adicionar_membros(self, membro):
        self.membros.append(membro)

    def listar_membros(self):
        print(f"\033[0;34mMembros da Biblioteca {self.nome}:\033[m")
        for i, membro in enumerate(self.membros):
            print(f"{i}: {membro}")  
    
    def remover_membros(self):
        print(f"\033[0;34mREMOVER MEMBRO\033[m")
        for i, membro in enumerate(self.membros):
            print(f"{i}: {membro}")
        while True:
            try:
                indice = int(input("Digite o número do membro que você deseja remover: "))
                if 0 <= indice < len(self.membros):
                    membro_removido = self.membros.pop(indice)
                    print(f"{membro_removido} removido.")
                    break
                else:
                    print("Digite um número válido correspondente ao membro.")
            except (ValueError, TypeError):
                print(f'\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
                continue
            except (KeyboardInterrupt):
                print(f'\033[0;31mERRO:Operação canelada pelo usuário=\033[m')
                return 0
    
    def registrar_empréstimo(self, livro, membro):
        print("emprestimo")
        if livro in self.catálogo_de_livros:
            livro.emprestado = True
            print(f"Empréstimo realizado com sucesso: {livro.get_título()} emprestado para {membro}")
        else:
            print("Livro não disponível para empréstimo.")

    def registrar_devolucao(self, livro, membro):
        if livro in self.catálogo_de_livros and livro.emprestado:
            livro.emprestado = False
            print(f"Devolução realizada com sucesso: {livro.get_título()} devolvido por {membro}")
        else:
            print("Este livro não está emprestado ou não faz parte do catálogo da biblioteca.")

    def pesquisar_livro(self, termo_pesquisa):
        resultados_pesquisa = []
        for livro in self.catálogo_de_livros:
            if termo_pesquisa.lower() in livro.get_título().lower() or termo_pesquisa.lower() in livro.get_autor().lower() or str(termo_pesquisa) == str(livro.get_ID()):
                resultados_pesquisa.append(livro)
        return resultados_pesquisa

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

if __name__ == "__main__":
    biblioteca = Biblioteca("LABIRINTOS DO SABER")

from os import system

while True:
    resposta = menu(['Listar livros', 'Adicionar livro', 'Remover livro', 'Listar membros', 'Adicionar membro', 'Remover membro', 'Registrar empréstimo', 'Registrar devolução', 'Pesquisar livro', 'Sair do sistema'])
    system("cls")
    match resposta:
        case 1:
            biblioteca.listar_livros()
        case 2:
            print(f"\033[0;34mADICIONAR LIVRO\033[m")
            título = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ID = int(input("Digite o ID do livro: "))
            descricao = input("Digite a descrição do livro: ")
            livro = Livro(título, autor, ID, descricao)
            biblioteca.adicionar_livros(livro)
            print("Livro adicionado com sucesso.")
        case 3:
            biblioteca.remover_livros()
        case 4:
            biblioteca.listar_membros()
        case 5:
            print(f"\033[0;34mADICIONAR MEMBRO\033[m")
            nome = input("Digite o nome do membro: ")
            biblioteca.adicionar_membros(nome)
            print("Membro adicionado com sucesso.")
        case 6:
            biblioteca.remover_membros()
        case 7:
            print(f"\033[0;34mREGISTRO DE EMPRÉSTIMO\033[m")
            biblioteca.listar_livros()
            biblioteca.listar_membros()
            livro_idx = int(input("Digite o índice do livro: "))
            membro_idx = int(input("Digite o índice do membro: "))
            livro = biblioteca.catálogo_de_livros[livro_idx]
            membro = biblioteca.membros[membro_idx]
            biblioteca.registrar_empréstimo(livro, membro)
        case 8:
            print(f"\033[0;34mREGISTRO DE DEVOLUÇÃO\033[m")
            biblioteca.listar_livros()
            biblioteca.listar_membros()
            livro_idx = int(input("Digite o índice do livro: "))
            membro_idx = int(input("Digite o índice do membro: "))
            livro = biblioteca.catálogo_de_livros[livro_idx]
            membro = biblioteca.membros[membro_idx]
            biblioteca.registrar_devolucao(livro, membro)
        case 9:
            print(f"\033[0;34mPESQUISAR LIVROS\033[m")
            termo_pesquisa = input("Digite o título, autor ou ID do livro que deseja pesquisar: ")
            resultados_pesquisa = biblioteca.pesquisar_livro(termo_pesquisa)
            if resultados_pesquisa:
                print("Resultados da pesquisa:")
                for livro in resultados_pesquisa:
                    print(livro)
            else:
                print("Nenhum livro encontrado com o termo de pesquisa fornecido.")
        case 10:
            print("Encerrando o programa...")
            break
        case _:
            print('\033[0;30;41mERRO! Digite uma opção válida!\033[m')
    