def dobro2(x):
    return x * 2

def multi_pi(x):
    mult_pi = x * PI()
    return mult_pi
# Funcao com retorno
def PI():
   return 3.1415

def imprimir_lista(lista: list):
    for x in lista:
        print("Elemento: ", x)

# Criar uma função com valor padrao
def boas_vindas2(nome="Fulano"):
    print(f"Seja bem-vind@ {nome}!")


# Essa funcao recebe 1 parametro
def boas_vindas(nome: str, sobrenome: str, idade: int, cores: list):
    print(f"Seja bem-vind@ {nome} {sobrenome}, você tem {idade} anos!")
    print("Você gosta das cores: ", cores)
    print("Estamos aprendendo Python")


# Chamada de função
lista_cores = ["Azul", "Verde"]
# boas_vindas(sobrenome = "Carvalho", nome = "Mário",  idade = 24, cores = lista_cores) # na chamada da função, mandamos 1 argumento
# boas_vindas(idade = 26, nome = "Pedro", sobrenome = "Carvalho",  cores = 1997) # na chamada da função, mandamos 1 argumento
# boas_vindas(nome = "Rebeca", sobrenome = "Carvalho", idade = 27, cores = 1997) # na chamada da função, mandamos 1 argumento

#boas_vindas2("Lucas")
#boas_vindas2("Elisa")
#boas_vindas2()

frutas = ["Uva", "Pêra", "Maça"]
#imprimir_lista("Python")
#imprimir_lista(frutas)

pi = PI()
x = multi_pi(2)
print("Multi PI: ", x)
print("PI: ", pi)