# Importação da lib tkinter
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.widget1 = Frame(master)
        self.widget1["pady"] = 10
        self.widget1.pack()
       
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        
        self.sair = Button(self.widget1, text="Sair")
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        # PEgando o click
        self.sair["command"] = self.widget1.quit
        self.sair.pack ()

        self.cadastrar = Button(self.widget1, text="Cadastrar")
        self.cadastrar["font"] = ("Calibri", "10")
        self.cadastrar["width"] = 10
        # Pegando o click e chamando a funcao
        self.cadastrar["command"] = self.cadastrar
        self.cadastrar.pack ()

        self.resultado = Label(self.widget1, text="", font=self.fontePadrao)
        self.resultado["font"] = ("Verdana", "10", "italic", "bold")
        self.resultado.pack()

    def cadastrar(self):
        self.resultado["text"] = "Cadastro realizado"

root = Tk()
Application(root)
root.mainloop()