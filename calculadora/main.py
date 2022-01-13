import matematica as m
from matematica import *

import camelcase


print(mult(4,8))
c = camelcase.CamelCase()
txt = "meu nome é mario"
print(c.hump(txt))

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

soma = soma(n1, n2)
sub = sub(n1, n2)
div = div(n1, n2)
mult = mult(n1, n2)

print(f"{n1} + {n2} == ", soma)
print(f"{n1} - {n2} == ", sub)
print(f"{n1} / {n2} == ", div)
print(f"{n1} * {n2} == ", mult)