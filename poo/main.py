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

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
    def comer(self, alimento):
        print(f"A pessoa {self.nome} está comento {alimento}")

pessoa = Pessoa("Mário", 24)
pessoa.comer("Maça")
print(pessoa)