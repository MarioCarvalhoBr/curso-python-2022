# Faça um programa que receba dois números inteiros e gere os
#  números inteiros que estão no intervalo compreendido por eles.
# (Use range deintervalos (range(x, y))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 < num2:
    lista_fechada = []
    for x in range(num1, num2 + 1):
        lista_fechada.append(x)
    print("Lista fechada: ", lista_fechada)

    lista_aberta = []
    for x in range(num1 + 1, num2):
        lista_aberta.append(x)
    print("Lista aberta: ", lista_aberta)
else:
    print("Não é possível gerar números nesse intervalo!")
