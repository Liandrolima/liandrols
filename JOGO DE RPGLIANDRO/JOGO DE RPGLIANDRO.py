import tkinter as tk
from tkinter import ttk
import pygame
from tkinter import messagebox
import sqlite3
import random

class PersistenciaDados:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS personagens
                        (id INTEGER PRIMARY KEY, nome TEXT, classe TEXT, nivel INTEGER, pontos_vida INTEGER)''')

    def salvar_personagem(self, personagem):
        self.c.execute("INSERT INTO personagens (nome, classe, nivel, pontos_vida) VALUES (?, ?, ?, ?)",
                       (personagem.nome, personagem.classe, personagem.nivel, personagem.pontos_vida))
        self.conn.commit()

    def carregar_personagem(self, id_personagem):
        self.c.execute("SELECT * FROM personagens WHERE id=?", (id_personagem,))
        data = self.c.fetchone()
        if data:
            return Personagem(data[1], data[2], data[3], data[4])
        else:
            messagebox.showerror("Erro", "Personagem não encontrado.")
            return None

    def fechar_conexao(self):
        self.conn.close()

class Personagem:
    def __init__(self, nome, classe, nivel=1, pontos_vida=100):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = pontos_vida

    def mostrar_info(self):
        messagebox.showinfo("Informações do Personagem", f"Nome: {self.nome}\nClasse: {self.classe}\nNível: {self.nivel}\nPontos de Vida: {self.pontos_vida}")

def criar_personagem():
    global entry_nome, entry_classe
    nome = entry_nome.get()
    classe = entry_classe.get()
    personagem = Personagem(nome, classe)
    db.salvar_personagem(personagem)
    messagebox.showinfo("Sucesso", "Personagem criado e salvo com sucesso!")

def carregar_personagem():
    global entry_id
    id_personagem = entry_id.get()
    personagem = db.carregar_personagem(id_personagem)
    if personagem:
        personagem.mostrar_info()

def batalha(personagem):
    pontos_vida_inimigo = random.randint(50, 100)
    messagebox.showinfo("Início da Batalha", f"Batalha começou!\nPontos de Vida do inimigo: {pontos_vida_inimigo}")
    while personagem.pontos_vida > 0 and pontos_vida_inimigo > 0:
        dano = random.randint(10, 20)
        messagebox.showinfo("Ataque", f"{personagem.nome} ataca e causa {dano} de dano!")
        pontos_vida_inimigo -= dano
        messagebox.showinfo("Pontos de Vida do Inimigo", f"Pontos de Vida do inimigo: {pontos_vida_inimigo}")
        if pontos_vida_inimigo <= 0:
            messagebox.showinfo("Fim da Batalha", rf"GRANDE VITÓRIA {personagem.nome} \nRECEBA O SEU \N🏆")
            personagem.nivel += 1
            messagebox.showinfo("Nível", f"{personagem.nome} subiu para o nível {personagem.nivel}!")
            break
        dano_inimigo = random.randint(5, 15)
        messagebox.showinfo("Ataque do Inimigo", f"Inimigo ataca e causa {dano_inimigo} de dano!")
        personagem.pontos_vida -= dano_inimigo
        messagebox.showinfo("Pontos de Vida do Personagem", f"Pontos de Vida de {personagem.nome}: {personagem.pontos_vida}")
        if personagem.pontos_vida <= 0:
            messagebox.showinfo("Fim da Batalha", f"{personagem.nome} foi derrotado.")

    
def iniciar_jogo():
    global entry_id
    id_personagem = entry_id.get()
    personagem = db.carregar_personagem(id_personagem)
    if personagem:
        batalha(personagem)

def sair_jogo():
    db.fechar_conexao()
    messagebox.showinfo("Saída", "O jogo foi encerrado.")
    exit()

def menu_principal():
    global entry_nome, entry_classe, entry_id
    janela = tk.Tk()
    janela.title("Batalha de Midway")
    janela.geometry("500x300+100+100")
    janela.configure(bg="#4B5320") 

    estilo = ttk.Style()   
    estilo.configure('.', borderwidth=10, relief='rounded', foreground='white', background='#4B5320')
    estilo.map('.', background=[('active', '#4B5320')])
    
    frame = ttk.Frame(janela, width=500, height=300)
    frame.pack()
    caminho_musica = r"C:\\Users\\Administrador.DESKTOP-PSGO920\\Desktop\\LIMA\\ex021.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)
    
    imagem_gif = tk.PhotoImage(file="C:\\Users\\Administrador.DESKTOP-PSGO920\\Desktop\\LIMA\\giphy.gif")
    label_imagem = tk.Label(janela, image=imagem_gif)
    label_imagem.pack()    

    label_nome = tk.Label(frame, text="Nome:", bg="#4B5320")
    label_nome.grid(row=0, column=0)
    entry_nome = tk.Entry(frame)
    entry_nome.grid(row=0, column=1)

    label_classe = tk.Label(frame, text="Classe:", bg="#4B5320")
    label_classe.grid(row=1, column=0)
    entry_classe = tk.Entry(frame)
    entry_classe.grid(row=1, column=1)

    button_criar_personagem = tk.Button(frame, text="Criar Personagem", command=criar_personagem, bg="#4B5320")
    button_criar_personagem.grid(row=2, columnspan=2)

    label_id = tk.Label(frame, text="ID do Personagem:", bg="#4B5320")
    label_id.grid(row=3, column=0)
    entry_id = tk.Entry(frame)
    entry_id.grid(row=3, column=1)

    button_carregar_personagem = tk.Button(frame, text="Carregar Personagem", command=carregar_personagem, bg="#4B5320")
    button_carregar_personagem.grid(row=4, columnspan=2)

    button_iniciar_jogo = tk.Button(frame, text="Iniciar Jogo", command=iniciar_jogo, bg="#4B5320")
    button_iniciar_jogo.grid(row=5, columnspan=2)

    button_sair_jogo = tk.Button(frame, text="Sair", command=sair_jogo, bg="#4B5320")
    button_sair_jogo.grid(row=6, columnspan=2)

    janela.mainloop()

if __name__ == "__main__":
    db = PersistenciaDados('Liandro_rpg.db')
    menu_principal()
