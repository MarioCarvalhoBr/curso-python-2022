from animal import Animal
class Ave(Animal):
    def __init__(self, bico, nome):
        super().__init__(nome)
        self.bico = bico

    def __str__(self) -> str:
        return super().__str__() + ", bico: "+self.bico

    def porOvos(self):
        print(f"O animal {self.nome} põe ovos!")