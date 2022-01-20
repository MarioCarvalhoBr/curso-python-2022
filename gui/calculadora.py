# Importação da lib tkinter
from tkinter import *
class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.titulo = Label(self.container1, text="CALCULADORA")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_num1 = Label(self.container1, text="Número 1: ")
        self.lbl_num1["font"] = ("Arial", "10", "bold")
        self.lbl_num1.pack(side=LEFT)

        self.txt_num1 = Entry(self.container1)
        self.txt_num1["width"] = 30
        self.txt_num1["font"] = ("Arial", "10", "bold")
        self.txt_num1.pack(side=LEFT)

        self.lbl_num2 = Label(self.container2, text="Número 2: ")
        self.lbl_num2["font"] = ("Arial", "10", "bold")
        self.lbl_num2.pack(side=LEFT)

        self.txt_num2 = Entry(self.container2)
        self.txt_num2["width"] = 30
        self.txt_num2["font"] = ("Arial", "10", "bold")
        self.txt_num2.pack(side=LEFT)

        self.autenticar = Button(self.container3)
        self.autenticar["text"] = "+"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 5
        self.autenticar["command"] = self.soma
        self.autenticar.pack(side=LEFT)

        self.lbl_resultado = Label(self.container4, text="")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

    def soma(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        soma = num1 + num2
        self.lbl_resultado["text"] = f"{num1} + {num2} == {soma}"
root = Tk()
Application(root)
root.mainloop()