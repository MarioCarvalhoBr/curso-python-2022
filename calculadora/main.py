import matematica as m
from matematica import *

import camelcase


print(mult(4,8))
c = camelcase.CamelCase()
txt = "meu nome é mario"
print(c.hump(txt))
try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    soma = soma(n1, n2)
    sub = sub(n1, n2)
    div = div2(n1, n2)
    mult = mult(n1, n2)

    print(f"{n1} + {n2} == ", soma)
    print(f"{n1} - {n2} == ", sub)
    print(f"{n1} / {n2} == ", div)
    print(f"{n1} * {n2} == ", mult)
except ValueError:
    print("Você inseriu um valor não numérico!")
except:
    print("Erro ao entrar com os dados!")
