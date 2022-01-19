class Animal:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self) -> str:
        return self.nome

    def locomover(self):
        print(f"O animal {self.nome} está se locomovendo!")