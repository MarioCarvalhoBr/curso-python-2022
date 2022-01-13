#calculadora usando função

#Definindo as funções de cada operação
def soma (n1, n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mult (n1,n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

op = input("escolha a operação, +, -, * ou /")

n1 = float(input("Digite um numero"))
n2 = float(input("Digite outro numero"))

if op == "+":
    valor = soma(n1,n2)
    print(f"a soma de {n1} + {n2} e:", valor)

elif op == "-":
    valor = sub(n1,n2)
    print(f"a soma de {n1} - {n2} e:", valor)

elif op == "*" :
    valor = mult(n1,n2)
    print(f"a soma de {n1} * {n2} e:", valor)

elif op == "/" :
    valor = div(n1,n2)
    print(f"a soma de {n1} / {n2} e:", valor)