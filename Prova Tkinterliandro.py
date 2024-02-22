from tkinter import *

janela = Tk()
janela.title("Conversor de Unidade")

final = StringVar()

janela.geometry("250x300")
janela.resizable(False, False)
titulo = Label(janela, text="Comprimento", width=20, height=0, padx=0, font=("Ivy 12 bold"))
titulo.pack()
numr = Entry(janela, bg="lightblue")
numr.pack()
label_resultado = Label(janela, width=16, height=3, textvariable=final, font=("Arial 10 bold"), background="grey")
label_resultado.place(x=56, y=50) 

def apagar():
    numr.delete(0, END)

def btclik(numero):
    num = numr.get()
    numr.delete(0, END)
    numr.insert(END, str(num) + str((numero)))

def metro_to_centimetro():
    try:
        metro = float(numr.get())
        centimetros = metro *100
        final.set(f"{metro:.2f}m é igual a \n{centimetros:.2f}cm")
    except ValueError:
        final.set("Erro: \nInsira um valor válido")

def centimetros_to_metro():
    try:
        centimetros = float(numr.get())
        metro = centimetros / 100
        final.set(f"{centimetros:.2f}cm é igual a \n{metro:.2f}m")
    except ValueError:
        final.set(f"Erro: \nInsira um valor válido")