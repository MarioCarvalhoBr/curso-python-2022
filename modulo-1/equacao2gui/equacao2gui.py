from tkinter import *
import funcoes
class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1["padx"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3.pack()

        self.titulo = Label(self.container1, text="CALCULA EQUAÇÂO 2-grau")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_a = Label(self.container1, text="a: ")
        self.lbl_a["font"] = ("Arial", "10", "bold")
        self.lbl_a.pack(side=LEFT)

        self.txt_a = Entry(self.container1)
        self.txt_a["width"] = 10
        self.txt_a["font"] = ("Arial", "10", "bold")
        self.txt_a.pack(side=LEFT)

        self.lbl_b = Label(self.container1, text="b: ")
        self.lbl_b["font"] = ("Arial", "10", "bold")
        self.lbl_b.pack(side=LEFT)

        self.txt_b = Entry(self.container1)
        self.txt_b["width"] = 10
        self.txt_b["font"] = ("Arial", "10", "bold")
        self.txt_b.pack(side=LEFT)

        self.lbl_c = Label(self.container1, text="c: ")
        self.lbl_c["font"] = ("Arial", "10", "bold")
        self.lbl_c.pack(side=LEFT)

        self.txt_c = Entry(self.container1)
        self.txt_c["width"] = 10
        self.txt_c["font"] = ("Arial", "10", "bold")
        self.txt_c.pack(side=LEFT)

        self.btn_calcular = Button(self.container2)
        self.btn_calcular["text"] = "Calcular"
        self.btn_calcular["font"] = ("Calibri", "15")
        self.btn_calcular["width"] = 10
        self.btn_calcular["command"] = self.calcular
        self.btn_calcular.pack(side=LEFT)

        self.lbl_delta = Label(self.container3, text="Delta: ")
        self.lbl_delta["font"] = ("Arial", "10", "bold")
        self.lbl_delta.pack()

        self.lbl_x1 = Label(self.container3, text="X1: ")
        self.lbl_x1["font"] = ("Arial", "10", "bold")
        self.lbl_x1.pack()

        self.lbl_x2 = Label(self.container3, text="X2: ")
        self.lbl_x2["font"] = ("Arial", "10", "bold")
        self.lbl_x2.pack()

    def calcular(self):
        a = float(self.txt_a.get())
        b = float(self.txt_b.get())
        c = float(self.txt_c.get())

        delta = funcoes.delta(a, b, c)
        self.lbl_delta["text"] = f"Delta == {delta}"
        if delta >= 0:
            x1 = funcoes.raiz_x1(a, b, delta)
            x2 = funcoes.raiz_x2(a, b, delta)

            self.lbl_x1["text"] = f"X1 == {x1}"
            self.lbl_x2["text"] = f"X2 == {x2}"
        else:
            self.lbl_x1["text"] = f"Não existem raízes reais"
            self.lbl_x2["text"] = ""
root = Tk()
Application(root)
root.mainloop()