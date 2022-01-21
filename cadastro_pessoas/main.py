from tkinter import *
import pandas as pd


class Application:
    def __init__(self, master=None):
        self.master = master
        self.banco_pessoas = pd.read_csv("cadastro_pessoas/banco.csv", sep=";")
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

        self.container5 = Frame(master)
        self.container5["pady"] = 10
        self.container5.pack()

        self.titulo = Label(self.container1, text="CADASTRO DE PESSOAS")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_cpf = Label(self.container1, text="CPF: ")
        self.lbl_cpf["font"] = ("Arial", "10", "bold")
        self.lbl_cpf.pack(side=LEFT)

        self.txt_cpf = Entry(self.container1)
        self.txt_cpf["width"] = 30
        self.txt_cpf["font"] = ("Arial", "10", "bold")
        self.txt_cpf.pack(side=LEFT)

        self.lbl_nome = Label(self.container2, text="Nome: ")
        self.lbl_nome["font"] = ("Arial", "10", "bold")
        self.lbl_nome.pack(side=LEFT)

        self.txt_nome = Entry(self.container2)
        self.txt_nome["width"] = 30
        self.txt_nome["font"] = ("Arial", "10", "bold")
        self.txt_nome.pack(side=LEFT)

        self.lbl_idade = Label(self.container3, text="Idade: ")
        self.lbl_idade["font"] = ("Arial", "10", "bold")
        self.lbl_idade.pack(side=LEFT)

        self.txt_idade = Entry(self.container3)
        self.txt_idade["width"] = 30
        self.txt_idade["font"] = ("Arial", "10", "bold")
        self.txt_idade.pack(side=LEFT)

        self.btn_add_pessoa = Button(self.container4)
        self.btn_add_pessoa["text"] = "Adicionar"
        self.btn_add_pessoa["font"] = ("Calibri", "15")
        self.btn_add_pessoa["width"] = 10
        self.btn_add_pessoa["command"] = self.add_pessoa
        self.btn_add_pessoa.pack()

        self.lbl_resultado = Label(self.container4, text="Lista de pessoas: ")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

        #
        self.init_tabela()

    def init_tabela(self):
        self.lbl_resultado["text"] = f"Lista de pessoas: \n{self.banco_pessoas.to_string()}"
        # code for creating table

        lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

        total_rows = len(lst)
        total_columns = len(lst[0])
            
        for i in range(total_rows):
            for j in range(total_columns):       
                self.e = Entry(self.container5, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
                
    def add_pessoa(self):
        cpf = self.txt_cpf.get()
        nome = self.txt_nome.get()
        idade = self.txt_idade.get()

        linha = {'CPF': cpf,
               'Nome': nome,
               'Idade': idade}

        self.banco_pessoas = self.banco_pessoas.append(linha, ignore_index=True)
        self.banco_pessoas.to_csv('cadastro_pessoas/banco.csv', sep=";", index=False)
        
        self.init_tabela()
        print(self.banco_pessoas.shape)

root = Tk()
root.title('SISTEMA DE CADASTRO')
root.geometry("500x500")
root.eval('tk::PlaceWindow . center')

Application(root)
root.mainloop()
