from tkinter import *

janela = Tk()
janela.title("Login")
janela.geometry("400x320")

def realizar_login():
    senha = entry_senha.get()
    e_mail = entry_e_mail.get()
    
    if len(senha) > 6 and "@" in e_mail:
        label_senha_re["text"] = "Login realizado com sucesso!"
        label_senha_re["fg"] = "green"
        label_senha_re["bg"] = "lightyellow"
        label_e_mail_re["text"] = ""
    else:
        label_senha_re["text"] = "Erro: senha precisa ter mais de 6 dígitos ou \ne-mail inválido."
        label_senha_re["fg"] = "red"
        label_senha_re["bg"] = "lightyellow"
        label_e_mail_re["text"] = ""

    entry_senha.delete(0, END)
    entry_e_mail.delete(0, END)

label_fazer_login = Label(janela, text="Fazer Login", font=("Arial 14 bold"))
label_fazer_login.grid(row=0, column=0, columnspan=2, pady=(20,10))

label_senha = Label(janela, width=10, height=2, text="Senha: ", font=("Arial 10"), anchor="w")
label_senha.grid(row=1, column=0, padx=10, pady=(30, 5), sticky=NSEW)
entry_senha = Entry(janela, width=30, font=("Arial 10"))
entry_senha.grid(row=1, column=1, padx=10, pady=(30, 5), sticky=W)

label_e_mail = Label(janela, width=10, height=2, text="E-mail: ", font=("Arial 10"), anchor="w")
label_e_mail.grid(row=2, column=0, padx=10, pady=(10, 5), sticky=NSEW)
entry_e_mail = Entry(janela, width=30, font=("Arial 10"), state="normal")
entry_e_mail.grid(row=2, column=1, padx=10, pady=(10, 5), sticky=W)

label_senha_re = Label(janela, width=30, height=2, text="", font=("Arial 10"), anchor="center")
label_senha_re.grid(row=3, column=0, columnspan=2, padx=10, pady=(20, 10), sticky=NSEW)
label_senha_re["bg"] = "blue"

label_e_mail_re = Label(janela, width=30, height=2, text="", font=("Arial 10"), anchor="center")
label_e_mail_re.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 20), sticky=NSEW)



botao = Button(janela, command=realizar_login, width=10, height=2, text="Login", relief="raised", bg="white")
botao.place(x=140, y=260)

janela.mainloop()
