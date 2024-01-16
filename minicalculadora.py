from tkinter import *

def somar():
    v1 = int(caixa1.get())
    v2 = int(caixa2.get())
    soma = v1 + v2
    l3.set(soma)
    print("Resultado: ", soma)


def subtrair():
    v1 = int(caixa1.get())
    v2 = int(caixa2.get())
    subtracao = v1 - v2
    l3.set(subtracao)
    print("Resultado: ", subtracao)
    

def dividir():
    v1 = int(caixa1.get())
    v2 = int(caixa2.get())
    dividir = v1 / v2
    l3.set(dividir)
    print("Resultado: ", dividir)


def multiplicar():
    v1 = int(caixa1.get())
    v2 = int(caixa2.get())
    multiplicar = v1 * v2
    l3.set(multiplicar)
    print("Resultado: ", multiplicar)


janela = Tk()
janela.title("Calculadora")
janela.iconbitmap("Calculator_30001.ico")
janela.geometry("300x250+100+50")
# janela.metodo(largura, altura)
janela.resizable(False, False)
l3 = StringVar()


num1 = Label(janela,
             text="Primeiro valor: ",
             font=("Arial",12))

caixa1 = Entry(width=12)

num2 = Label(janela,
             text="Segundo valor: ",
             font=("Arial",12))
caixa2 = Entry(width=12)
numr = Label(janela,
             text="",
             font=("Arial",12))
btnSomar = Button(text="➕", command=somar)
btnSubtrair = Button(text="➖", command=subtrair)
btnDividir = Button(text="➗", command=dividir)
btnMultiplicar = Button(text="✖", command=multiplicar)
label3 = Label(fg="red", font=("Arial", 20), textvariable=l3)

num1.pack()
caixa1.pack()
num2.pack()
caixa2.pack()

btnSomar.pack()
btnSubtrair.pack()
btnDividir.pack()
btnMultiplicar.pack()
numr.pack()
label3.pack()
janela.mainloop()
