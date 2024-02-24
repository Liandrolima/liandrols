class Elevador:
    def __init__(self,totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar
    
    def Subir(self):
        if self.atualAndar != self.totalAndar:
            print(f"Você está no {self.atualAndar}º andar", "Subindo")
        else:
            print("VOCÊ ESTA NO ANDAR MAIS ALTO")
    def Descer(self):
        if self.atualAndar != 0:
            print(f"Você está no {self.atualAndar}º andar", "Descendo")
        if self.atualAndar == 0:
            print("VOCÊ ESTÁ NO TÉRREO")
    
    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print(f"O elevador está com {self.atualCapacidade} pessoa(s)")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")
    
    def Sair(self):
        if self.atualCapacidade >= 1:
            print(f"O elevador está com {self.atualCapacidade} pessoa(s)", "Saindo uma pessoa")
        if self.atualCapacidade == 0:
            print("NÃO TEM NINGUÉM")

elevador = Elevador(totalCapacidade=10, atualCapacidade=0, totalAndar=20, atualAndar=0)
elevador.Subir()
elevador.Descer()
elevador.Entrar()
elevador.Sair()
