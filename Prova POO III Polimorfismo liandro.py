class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        if self.valor_litro == 0:
            print("Valor do litro não está definido.")
            return
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
            print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    def abastecer_por_litro(self, litros):
        if litros > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
        else:
            valor_a_pagar = litros * self.valor_litro
            print(f"Quantidade abastecida: {litros:.2f} litros de {self.tipo_combustivel}.")
            print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")
            self.quantidade_combustivel -= litros
            print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    
    def alterar_Valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"O novo valor do litro {self.tipo_combustivel} é R$ {novo_valor:.2f}")
    
    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        print(f"O novo tipo de cobustível é: {novo_combustivel}")