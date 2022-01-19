from animal import Animal
class Mamifero(Animal):
    def __init__(self, pelo, nome):
        super().__init__(nome)
        self.pelo = pelo

    def __str__(self) -> str:
        return super().__str__() + ", pelos: "+self.pelo

    def mamar(self):
        print(f"O animal {self.nome} mama!")