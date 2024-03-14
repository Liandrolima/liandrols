import hashlib
import sqlite3
import csv
import json
from bs4 import BeautifulSoup
from datetime import datetime

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha = hashlib.sha256(senha.encode()).hexdigest()

class GerenciadorUsuarios:
    def __init__(self):
        self.conexao = sqlite3.connect('banco_dados.db')
        self.cursor = self.conexao.cursor()
        self._criar_tabela_usuarios()

    def _criar_tabela_usuarios(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                username TEXT NOT NULL UNIQUE,
                                senha TEXT NOT NULL)''')
        self.conexao.commit()

    def cadastrar_usuario(self, nome, username, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.cursor.execute("INSERT INTO usuarios (nome, username, senha) VALUES (?, ?, ?)", (nome, username, senha_hash))
        self.conexao.commit()
        
    def autenticar_usuario(self, username, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM usuarios WHERE username=? AND senha=?", (username, senha_hash))
        return self.cursor.fetchone() is not None

    def fechar_conexao(self):
        self.conexao.close()


class GerenciadorListaEmails:
    def __init__(self):
        self.conexao = sqlite3.connect('banco_dados.db')
        self.cursor = self.conexao.cursor()
        self._criar_tabela_clientes()

    def _criar_tabela_clientes(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE)''')
        self.conexao.commit()

    def adicionar_cliente(self, nome, email):
        self.cursor.execute("SELECT * FROM clientes WHERE email=?", (email,))
        cliente_existente = self.cursor.fetchone()
        if cliente_existente:
            print("Este email já está registrado na lista.")
        else:
            try:
                self.cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
                self.conexao.commit()
                print(f"Cliente {nome} adicionado com sucesso!")
            except sqlite3.IntegrityError:
                print("Ocorreu um erro ao adicionar o cliente.")

    
    def remover_cliente(self, email):
        self.cursor.execute("DELETE FROM clientes WHERE email=?", (email,))
        if self.cursor.rowcount > 0:
            print("Cliente removido com sucesso!")
        else:
            print("Email não encontrado na lista.")
        self.conexao.commit()

    def exibir_lista(self):
        self.cursor.execute("SELECT nome, email FROM clientes")
        lista_clientes = self.cursor.fetchall()
        print("Lista de clientes:")
        for cliente in lista_clientes:
            print(f"Nome: {cliente[0]}, Email: {cliente[1]}")
        
    def importar_clientes_csv(self, arquivo):
        try:
            with open(arquivo, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Ignorar o cabeçalho
                for row in reader:
                    # Verificar se a linha contém dados válidos
                    if len(row) >= 2:
                        nome = row[0].strip().strip('" ,;')  # Removendo espaços em branco e aspas extras
                        email = row[1].strip().strip('" ,;')  # Removendo espaços em branco e aspas extras
                        self.adicionar_cliente(nome, email)
                    else:
                        print("Dados inválidos na linha:", row)
            print("Clientes importados com sucesso a partir do arquivo CSV.")
        except FileNotFoundError:
            print("O arquivo CSV especificado não foi encontrado.")

    def importar_clientes_html(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                soup = BeautifulSoup(file, 'html.parser')
                for tr in soup.find_all('tr'):
                    td_list = tr.find_all('td')
                    if td_list:
                        nome = td_list[0].text.strip()
                        email = td_list[1].text.strip()
                        self.adicionar_cliente(nome, email)
            print("Clientes importados com sucesso a partir do arquivo HTML.")
        except FileNotFoundError:
            print("O arquivo HTML especificado não foi encontrado.")

    def importar_clientes_json(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                data = json.load(file)
                for cliente in data['clientes']:
                    nome = cliente['nome']
                    email = cliente['email']
                    self.adicionar_cliente(nome, email)
            print("Clientes importados com sucesso a partir do arquivo JSON.")
        except FileNotFoundError:
            print("O arquivo JSON especificado não foi encontrado.")

    def fechar_conexao(self):
        self.conexao.close()

class EditorEmail:
    def criar_email_personalizado(self, cliente, conteudo, anexos=[]):
        email_personalizado = f"Para: {cliente.nome} <{cliente.email}>\n\n{conteudo}"
        if anexos:
            email_personalizado += "\n\nAnexos:"
            for anexo in anexos:
                email_personalizado += f"\n- {anexo}"
        print("Email personalizado criado com sucesso!")
        return email_personalizado, cliente


class AgendadorEmails:
    def __init__(self):
        self.agendamentos = []

    def agendar_email(self, cliente, conteudo, data_hora_envio):
        self.agendamentos.append((cliente, conteudo, data_hora_envio))
        print("Email agendado com sucesso!")

    def visualizar_agendamentos(self):
        print("Agendamentos de Email:")
        for i, (cliente, conteudo, data_hora_envio) in enumerate(self.agendamentos, start=1):
            print(f"{i}. Para: {cliente.nome}, Data e Hora: {data_hora_envio}")

    def disparar_emails(self):
        print("Disparando emails agendados...")
        for cliente, conteudo, data_hora_envio in self.agendamentos:
            print(f"Enviando email para {cliente.nome} em {data_hora_envio}:")
            print(f"Assunto: Email Agendado\nConteúdo: {conteudo}")
            print("Email enviado com sucesso!")
        self.agendamentos = []


class RelatoriosEstatisticas:
    def __init__(self):
        self.envios = []
        self.aberturas = []
        self.respostas = []

        # Conexão com o banco de dados
        self.conexao = sqlite3.connect('banco_dados.db')
        self.cursor = self.conexao.cursor()

        # Criação das tabelas
        self._criar_tabelas()

    def _criar_tabelas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS relatorio_entrega (
                                id INTEGER PRIMARY KEY,
                                cliente TEXT NOT NULL,
                                data_hora_envio TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS relatorio_abertura (
                                id INTEGER PRIMARY KEY,
                                cliente TEXT NOT NULL,
                                data_hora_abertura TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS relatorio_resposta (
                                id INTEGER PRIMARY KEY,
                                cliente TEXT NOT NULL,
                                data_hora_resposta TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS relatorio_conversao (
                                id INTEGER PRIMARY KEY,
                                cliente TEXT NOT NULL,
                                data_hora_abertura TEXT NOT NULL,
                                data_hora_resposta TEXT NOT NULL)''')

        self.conexao.commit()

    # Métodos para registrar os eventos e inserir os dados nas tabelas

    def registrar_envio(self, cliente, data_hora_envio):
        self.envios.append((cliente, data_hora_envio))
        print("Envio registrado com sucesso!")

    def registrar_abertura(self, cliente, data_hora_abertura):
        self.aberturas.append((cliente, data_hora_abertura))
        print("Abertura registrada com sucesso!")

    def registrar_resposta(self, cliente, data_hora_resposta):
        self.respostas.append((cliente, data_hora_resposta))
        print("Resposta registrada com sucesso!")

    def calcular_taxa_entrega(self):
        total_envios = len(self.envios)
        total_aberturas = len(self.aberturas)
        if total_envios > 0:
            taxa_entrega = (total_aberturas / total_envios) * 100
            return taxa_entrega
        else:
            return 0

    def calcular_taxa_abertura(self):
        total_envios = len(self.envios)
        total_aberturas = len(self.aberturas)
        if total_envios > 0:
            taxa_abertura = (total_aberturas / total_envios) * 100
            return taxa_abertura
        else:
            return 0

    def calcular_taxa_resposta(self):
        total_envios = len(self.envios)
        total_respostas = len(self.respostas)
        if total_envios > 0:
            taxa_resposta = (total_respostas / total_envios) * 100
            return taxa_resposta
        else:
            return 0

    def calcular_taxa_conversao(self):
        total_aberturas = len(self.aberturas)
        total_respostas = len(self.respostas)
        if total_aberturas > 0:
            taxa_conversao = (total_respostas / total_aberturas) * 100
            return taxa_conversao
        else:
            return 0

    def gerar_relatorio(self):
        print("Relatório de Estatísticas:")
        print(f"Taxa de Entrega: {self.calcular_taxa_entrega():.2f}%")
        print(f"Taxa de Abertura: {self.calcular_taxa_abertura():.2f}%")
        print(f"Taxa de Resposta: {self.calcular_taxa_resposta():.2f}%")
        print(f"Taxa de Conversão: {self.calcular_taxa_conversao():.2f}%")

    def inserir_relatorio_entrega(self):
        if self.envios:
            for cliente, data_hora_envio in self.envios:
                self.cursor.execute("INSERT INTO relatorio_entrega (cliente, data_hora_envio) VALUES (?, ?)", (cliente.nome, data_hora_envio))
                self.conexao.commit()
            print("Dados inseridos na tabela relatorio_entrega com sucesso!")
        else:
            print("Não há dados disponíveis para inserção no relatório de entrega.")

    def inserir_relatorio_abertura(self):
        for cliente, data_hora_abertura in self.aberturas:
            self.cursor.execute("INSERT INTO relatorio_abertura (cliente, data_hora_abertura) VALUES (?, ?)", (cliente.nome, data_hora_abertura))
            self.conexao.commit()

    def inserir_relatorio_resposta(self):
        for cliente, data_hora_resposta in self.respostas:
            self.cursor.execute("INSERT INTO relatorio_resposta (cliente, data_hora_resposta) VALUES (?, ?)", (cliente.nome, data_hora_resposta))
            self.conexao.commit()

    def inserir_relatorio_conversao(self):
        for cliente, data_hora_abertura in self.aberturas:
            for cliente_resp, data_hora_resposta in self.respostas:
                if cliente.nome == cliente_resp.nome:
                    self.cursor.execute("INSERT INTO relatorio_conversao (cliente, data_hora_abertura, data_hora_resposta) VALUES (?, ?, ?)", (cliente.nome, data_hora_abertura, data_hora_resposta))
                    self.conexao.commit()


class IntegracaoFerramentasTerceiros:
    def __init__(self):
        pass

    def integrar_automacao_marketing(self):
        print("Integrando com sistema de automação de marketing...")

    def integrar_crm(self):
        print("Integrando com CRM...")

    def integrar_analise_dados(self):
        print("Integrando com sistema de análise de dados...")

    def exportar_relatorio_csv(self, relatorio):
        print("Exportando relatório para CSV...")
        # Implementação para exportar o relatório para um arquivo CSV

    def exportar_relatorio_pdf(self, relatorio):
        print("Exportando relatório para PDF...")
        # Implementação para exportar o relatório para um arquivo PDF


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

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('          \033[30;42mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = teleInt('\033[36mSua opção: \033[m')
    return opc

if __name__ == "__main__":
    gerenciador_usuarios = GerenciadorUsuarios()
    autenticado = False
    
    while True:
        if not autenticado:
            opcao = menu(["Cadastrar novo usuário", "Autenticar usuário", "Sair"])
            if opcao == 1:
                print("Cadastro de novo usuário")
                while True:
                    nome = input("Nome: ")
                    username = input("Nome de usuário: ")
                    senha = input("Senha: ")
                    if gerenciador_usuarios.autenticar_usuario(username, senha):
                        print(f"Nome de usuário {username} já está em uso. Você será reconduzido ao menu principal para autenticação.")
                        break
                    else:
                        gerenciador_usuarios.cadastrar_usuario(nome, username, senha)
                        print(f"Nome de usuário {username} já está em uso. Você será reconduzido ao menu principal para autenticação.")
                        break
            elif opcao == 2:
                print("Autenticação de usuário")
                username = input("Digite seu nome de usuário: ")
                senha = input("Digite sua senha: ")
                if gerenciador_usuarios.autenticar_usuario(username, senha):
                    print("Autenticação bem-sucedida!")
                    autenticado = True
                else:
                    print("Nome de usuário ou senha incorretos.")
            elif opcao == 3:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            gerenciador_clientes = GerenciadorListaEmails()
            agendador = AgendadorEmails()
            relatorios = RelatoriosEstatisticas()
            integracao = IntegracaoFerramentasTerceiros()

            # Exemplos de clientes
            exemplos_clientes = [
                ("João Silva", "joao@exemplo.com"),
                ("Maria Oliveira", "maria@exemplo.com"),
                ("Carlos Santos", "carlos@exemplo.com"),
                ("Ana Pereira", "ana@exemplo.com"),
                ("Pedro Costa", "pedro@exemplo.com"),
                ("Juliana Lima", "juliana@exemplo.com"),
                ("Fernando Souza", "fernando@exemplo.com"),
                ("Amanda Almeida", "amanda@exemplo.com"),
                ("Lucas Oliveira", "lucas@exemplo.com"),
                ("Mariana Silva", "mariana@exemplo.com")
            ]
            
            # Adicionando os exemplos de clientes
            for nome, email in exemplos_clientes:
                gerenciador_clientes.adicionar_cliente(nome, email)

            while True:
                opcoes_permitidas = ["Adicionar cliente", "Remover cliente", 
                                     "Exibir lista de clientes", "Criar email personalizado", 
                                     "Agendar email", "Visualizar agendamentos", 
                                     "Disparar emails agendados", "Registrar envio", 
                                     "Gerar relatório de entrega", "Gerar relatório de abertura", 
                                     "Gerar relatório de resposta", "Gerar relatório de conversão", 
                                     "Exportar relatórios", "Integrar ferramentas de terceiros",
                                     "Importar clientes de CSV", "Importar clientes de HTML", "Importar clientes de JSON",
                                     "Sair"]
                
                opcao = menu(opcoes_permitidas)
                
                if opcao == 1:
                    print("Adicionar cliente")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    gerenciador_clientes.adicionar_cliente(nome, email)
                elif opcao == 2:
                    print("Remover cliente")
                    email = input("Email do cliente a ser removido: ")
                    gerenciador_clientes.remover_cliente(email)
                elif opcao == 3:
                    print("Exibir lista de clientes")
                    gerenciador_clientes.exibir_lista()
                if opcao == 4:
                    print("Criar email personalizado")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    conteudo = input("Conteúdo do email: ")
                    cliente = Cliente(nome, email)
                    editor = EditorEmail()
                    email_personalizado, cliente = editor.criar_email_personalizado(cliente, conteudo)  # Capturando o cliente retornado
                    gerenciador_clientes.adicionar_cliente(cliente.nome, cliente.email)
                elif opcao == 5:
                    print("Agendar email")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    conteudo = input("Conteúdo do email: ")
                    data_str = input("Data e hora do envio (formato: YYYY-MM-DD HH:MM): ")
                    data_hora_envio = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
                    cliente = Cliente(nome, email)
                    agendador.agendar_email(cliente, conteudo, data_hora_envio)
                elif opcao == 6:
                    print("Visualizar agendamentos")
                    agendador.visualizar_agendamentos()
                elif opcao == 7:
                    print("Disparar emails agendados")
                    agendador.disparar_emails()
                elif opcao == 8:
                    print("Registrar envio")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    cliente = Cliente(nome, email)
                    relatorios.registrar_envio(cliente, datetime.now())
                elif opcao == 9:
                    print("Gerar relatório de entrega")
                    relatorios.gerar_relatorio()
                    relatorios.inserir_relatorio_entrega()
                elif opcao == 10:
                    print("Gerar relatório de abertura")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    cliente = Cliente(nome, email)
                    relatorios.registrar_abertura(cliente, datetime.now())  # Exemplo de registro de abertura
                    relatorios.inserir_relatorio_abertura()
                elif opcao == 11:
                    print("Gerar relatório de resposta")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    cliente = Cliente(nome, email)
                    relatorios.registrar_resposta(cliente, datetime.now())  # Exemplo de registro de resposta
                    relatorios.inserir_relatorio_resposta()
                elif opcao == 12:
                    print("Gerar relatório de conversão")
                    nome = input("Nome do cliente: ")
                    email = input("Email do cliente: ")
                    cliente = Cliente(nome, email)
                    relatorios.registrar_abertura(cliente, datetime.now())  # Exemplo de registro de abertura
                    relatorios.registrar_resposta(cliente, datetime.now())  # Exemplo de registro de resposta
                    relatorios.inserir_relatorio_conversao()
                elif opcao == 13:
                    print("Exportar relatórios")
                    integracao.exportar_relatorio_csv(relatorios)  # Exemplo de exportação para CSV
                    integracao.exportar_relatorio_pdf(relatorios)  # Exemplo de exportação para PDF
                elif opcao == 14:
                    print("Integrar ferramentas de terceiros")
                    integracao.integrar_automacao_marketing()  # Exemplo de integração com automação de marketing
                    integracao.integrar_crm()  # Exemplo de integração com CRM
                    integracao.integrar_analise_dados()  # Exemplo de integração com análise de dados
                elif opcao == 15:
                    print("Importar clientes de CSV")
                    arquivo_csv = input("Digite o caminho do arquivo CSV: ")
                    gerenciador_clientes.importar_clientes_csv(arquivo_csv)
                elif opcao == 16:
                    print("Importar clientes de HTML")
                    arquivo_html = input("Digite o caminho do arquivo HTML: ")
                    gerenciador_clientes.importar_clientes_html(arquivo_html)
                elif opcao == 17:
                    print("Importar clientes de JSON")
                    arquivo_json = input("Digite o caminho do arquivo JSON: ")
                    gerenciador_clientes.importar_clientes_json(arquivo_json)
                elif opcao == 18:
                    autenticado = False
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

