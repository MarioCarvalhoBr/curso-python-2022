# Classe: Entidade/Projeto/Planta que gera os objetos
# Objeto: Gerado pela classe. Tem atributos e métodos.
# Atributos: Características do objeto (cor, altura, peso, nome, cpf, rg)
# Métodos: Ações que pode ser realizadas pelo objeto(andar(), comer() )

# Objeto do tipo lista
# nomeObjeto = nomeClasse(valores)
'''
lista1 = list()
lista2 = list((5,3,1,4,6))
lista3 = list((5,3,1,4,6))
lista4 = list((5,3,1,4,6))

lista1.sort()

print(lista1)
'''
"""

class Animal:
    def __init__(self, nome="Animal", idade=0, barulho_animal=""):
        # Atributos com valores padrão
        #eu.atributo = novo valor
        self.nome = nome
        self.idade = idade
        self.barulho_animal = barulho_animal
    
    def barulho(self):
        print(f"O animal {self.nome} faz {self.barulho_animal}")
    
    def __str__(self):
        return f"{self.nome};{self.idade}]"

dog = Animal("Cachorro", 14, "Auauau")
gato = Animal("Gato", 4, "Maiuuuu")

dog.barulho()
gato.barulho()
"""
class Pessoa:
    def __init__(self, cpf, nome, idade, cidade, genero):
        # Atributos
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero

    def __str__(self):
        return f"CPF: {self.cpf}, Nome: {self.nome}, Idade: {self.idade}, cidade: {self.cidade}, genero: {self.genero}"
    
    # Métodos -> Ações 
    def comer(self, alimento):
        print(f"A pessoa {self.nome} está comento {alimento}")
    def dormir(self):
        print(f"A pessoa {self.nome} está dormindo...")
    def jogar(self, jogo):
        print(f"A pessoa {self.nome} está jogando {jogo}")
    def estudar(self, texto):
        print(f"A pessoa {self.nome} está estudando {texto}")

class ListaPessoas:
    def __init__(self):
        self.lista = []
    def addPessoa(self, pessoa):
        self.lista.append(pessoa)
    def imprimir(self):
        for p in self.lista:
            print(p)

lista = ListaPessoas()
p1 = Pessoa(123, "maria", 12, "caruaru", "f")
lista.addPessoa(p1)
lista.addPessoa(p1)
lista.addPessoa(p1)
lista.addPessoa(p1)
lista.addPessoa(p1)

lista.imprimir()



banco_pessoas = []
while True:
    cpf = int(input("Digite o CPF: "))
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")
    genero = input("Digite o gênero: ")
    if cpf < 0:
        break
    else:
        pessoa = Pessoa(cpf, nome, idade, cidade, genero)
        banco_pessoas.append(pessoa)
        print("Pessoa inserida com sucesso!")

print("tipo banco_pessoas: ", type(banco_pessoas))
print("banco_pessoas: ", banco_pessoas)
for pessoa in banco_pessoas:
    print(pessoa)
    pessoa.comer("Maça")
    pessoa.dormir()
    pessoa.jogar("LOL")
    pessoa.estudar("Python")
    print("-"*25)
