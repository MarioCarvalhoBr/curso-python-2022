from mamifero import Mamifero
from ave import Ave

class Ornitorrinco(Ave, Mamifero):
    def __init__(self, pelo, bico, nome):
        Ave.__init__(self, bico, nome)
        Mamifero.__init__(self, pelo, nome)

    def mamar(self):
        super().mamar()
        print(f"O animal {self.nome} mama!")

    def porOvos(self):
        super().porOvos()
        print(f"O animal {self.nome} põe ovos!")

o1 = Ornitorrinco("Teste", "Grande", "Ornitorrinco")
o1.mamar()
print(o1)