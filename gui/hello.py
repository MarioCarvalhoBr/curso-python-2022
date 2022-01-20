# Importação da lib tkinter
from tkinter import *
# Tela
class Tela:
    # Receber a master root do TK
    def __init__(self, master=None):
        # Criação de um container
        self.container1 = Frame(master)
        # Registro do container
        self.container1.pack()
        # Criar um widget e adicionar ao container
        self.msg = Label(self.container1, text="Bem-vind@!")
        # Registro do widget
        self.msg.pack()

        self.container2 = Frame(master)
        # Registro do container
        self.container2.pack()

        # Criar um widget e adicionar ao container
        self.msg2 = Label(self.container2, text="Esse é um exemplo de label")
        # Registro do widget
        self.msg2.pack()


# Criar uma objeto do tipo Tk()
root = Tk()

# Passando o root pra minha classe
Tela(root)

# Event loop - verifica constantemente se outro evento foi acionado.
root.mainloop()