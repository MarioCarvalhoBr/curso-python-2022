class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    def __str__(self):
        return f"Nome: {self.nome }, endereco: {self.endereco}, "

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, endereco):
        super().__init__(nome, endereco)
        self.cpf = cpf
    def __str__(self):
        return f"Nome: {self.nome }, endereco: {self.endereco}, CPF: {self.cpf }\n"

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, endereco):
        super().__init__(nome, endereco)
        self.cnpj = cnpj
    def __str__(self):
        return  super().__str__() + f"CNPJ: {self.cnpj }\n"

p1 = PessoaFisica(123, "Mário", "Campo Grande")
p2 = PessoaFisica(456, "Elisa", "Caruaru")
p3 = PessoaJuridica(91838374738, "Lucas", "Caruaru")

print(p1)
print(p2)
print(p3)