# Ler uma lista de inteiros e criar uma nova lista de numeros pares
lista = [1,2,3,4,5,6,7,8,9,10,11]
nova_lista = []

for i in lista:
    if i % 2 == 0:
        nova_lista.append(i)

print("nova_lista: ", nova_lista)