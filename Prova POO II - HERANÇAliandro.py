class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
    
    def exibir_informacoes(self):
        print("Título:", self.titulo)
        print("Autor/Editora:", self.autor_ou_editora)

class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Gênero:", self.genero)

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Edição:", self.edicao)


print("\n" + "-"*30 + "\n")
livro = Livro("Romeu e Julieta", "William Shakespeare", "Elegia")
print("Detalhes do Livro:")
livro.exibir_informacoes()
print("\n" + "-"*30 + "\n")
revista = Revista("Os Lusíadas", " Luís Vaz de Camões", "12 de março de 1572")
print("\nDetalhes da Revista:")
revista.exibir_informacoes()
print("\n" + "-"*30 + "\n")