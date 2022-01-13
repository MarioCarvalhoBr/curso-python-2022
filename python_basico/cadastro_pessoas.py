# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    nova_pessoa = [nome, idade]
    lista_pessoas.append(nova_pessoa)
else:
    print("O cadastro de pessoas foi finalizado!")


for pessoa in lista_pessoas:
    print(f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos!")
else:
    print("A listagem de pessoas foi finalizado!")

print("Quantidade de pessoas cadastradas: ", len(lista_pessoas))
