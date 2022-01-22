#Crie um programa em Python que 
# calcule as raizes reais de uma equação do segundo grau.
import math

def delta (a,b,c):
    d = (b**2)-(4*a*c)
    return d

def raiz_x1(a,b,delta):
    x1 = (-b + math.sqrt(delta))/2*a
    return x1

def raiz_x2(a,b,delta):
    x2 = (-b - math.sqrt(delta))/2*a
    return x2