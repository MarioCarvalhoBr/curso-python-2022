def teste(x):
    if x % 3 == 0:
        return x
    else: 
        return 0
# Ler uma lista de inteiros e criar uma nova lista de numeros pares
lista = [1,2,3,4,5,6,7,8,9,10,11,12]
# newlist = [expression for item in iterable if condition == True]
nova_lista = [teste(i) for i in lista if i % 2 == 0]
nova_lista2 = [i for i in nova_lista if i != 0]

print("nova_lista: ", nova_lista)
print("nova_lista2: ", nova_lista2)